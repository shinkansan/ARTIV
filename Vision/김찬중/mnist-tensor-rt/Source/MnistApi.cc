#include <MnistApi.hh>

#include <cstddef>

using namespace std;
using nvinfer1::BuilderFlag;
using nvinfer1::createInferBuilder;
using nvinfer1::DataType;
using nvinfer1::DeviceType;
using nvinfer1::IBuilder;
using nvinfer1::IBuilderConfig;
using nvinfer1::ICudaEngine;
using nvinfer1::IExecutionContext;
using nvinfer1::INetworkDefinition;
using nvinfer1::LayerType;
using nvinfer1::NetworkDefinitionCreationFlag;
using nvinfer1::Weights;
using nvonnxparser::createParser;
using nvonnxparser::IParser;

bool MnistApi::Build()
{
    auto builder = _Unique<IBuilder> { nvinfer1::createInferBuilder(_logger) };
    if (!builder)
        return false;

    auto network = _Unique<INetworkDefinition> {
        builder->createNetworkV2(
            1u << static_cast<uint32_t>(
                NetworkDefinitionCreationFlag::kEXPLICIT_BATCH)),
    };
    if (!network)
        return false;

    auto config = _Unique<IBuilderConfig> { builder->createBuilderConfig() };
    if (!config)
        return false;

    auto parser = _Unique<IParser>(createParser(*network, _logger));
    if (!parser)
        return false;

    auto constructed = _ConstructNetwork(
        builder.get(), network.get(), config.get(), parser.get());
    if (!constructed)
        return false;

    _engine = _Shared<ICudaEngine> {
        builder->buildEngineWithConfig(*network, *config),
        _Deleter<ICudaEngine> {},
    };
    if (!_engine)
        return false;

    auto validation_result = _ValidateNetwork(network.get());
    if (!validation_result)
        return false;

    return true;
}

bool MnistApi::Infer()
{
    auto context
        = _Unique<IExecutionContext> { _engine->createExecutionContext() };
    if (!context)
        return false;

    // TODO

    return true;
}

bool MnistApi::CleanUp()
{
    // TODO

    return true;
}

bool MnistApi::_ConstructNetwork(IBuilder*           builder,
                                 INetworkDefinition* network,
                                 IBuilderConfig*     config,
                                 IParser*            parser)
{
    auto parsed = parser->parseFromFile(_param.filePath.c_str(),
                                        static_cast<int>(_logger.threashold()));
    if (!parsed)
        return false;

    builder->setMaxBatchSize(_param.batchSize);
    config->setMaxWorkspaceSize(_param.maxMemorySize);

    switch (_param.precision)
    {
    case Param::Precision::Fp16: {
        config->setFlag(BuilderFlag::kFP16);
        break;
    }
    case Param::Precision::Int8: {
        config->setFlag(BuilderFlag::kINT8);
        _SetAllTensorScales(network, 127.0f, 127.0f);
        break;
    }
    }

    auto dla_settings_set
        = _EnableDla(builder, config, _param.idxDlaCore, true);
    if (!dla_settings_set)
        return false;

    return true;
}

void MnistApi::_SetAllTensorScales(INetworkDefinition* network,
                                   float               in,
                                   float               out)
{
    for (int i = 0; i < network->getNbLayers(); ++i)
    {
        auto layer = network->getLayer(i);
        for (int j = 0; j < layer->getNbInputs(); ++j)
        {
            auto input = layer->getInput(j);
            if (input && !input->dynamicRangeIsSet())
                input->setDynamicRange(-in, in);
        }

        for (int j = 0; j < layer->getNbOutputs(); ++j)
        {
            auto output = layer->getOutput(j);
            if (output && !output->dynamicRangeIsSet())
            {
                if (layer->getType() == LayerType::kPOOLING)
                    output->setDynamicRange(-in, in);
                else
                    output->setDynamicRange(-out, out);
            }
        }
    }
}

bool MnistApi::_EnableDla(IBuilder*       builder,
                          IBuilderConfig* config,
                          int             idx_dla_core,
                          bool            allow_gpu_fallback)
{
    if (idx_dla_core < 0)
        return false;

    if (builder->getNbDLACores() == 0)
        return false;

    if (allow_gpu_fallback)
        config->setFlag(BuilderFlag::kGPU_FALLBACK);

    // INT8이 사용되지 않았을 떄
    if (!config->getFlag(BuilderFlag::kINT8))
    {
        // DLA 사용시 FP16 또는 INT8; FP32는 허용 안됨
        config->setFlag(BuilderFlag::kFP16);
    }

    config->setDefaultDeviceType(DeviceType::kDLA);
    config->setDLACore(idx_dla_core);
    config->setFlag(BuilderFlag::kSTRICT_TYPES);
}

bool MnistApi::_ValidateNetwork(INetworkDefinition* network)
{
    // Desired input: 1 * 1 * 28 * 28
    if (network->getNbInputs() != 1)
        return false;
    if (network->getInput(0)->getDimensions().nbDims != 4)
        return false;

    // Desired output: 1 * 10
    if (network->getNbOutputs() != 1)
        return false;
    if (network->getOutput(0)->getDimensions().nbDims != 2)
        return false;

    return true;
}