#ifndef __MNIST_TENSOR_RT_MNIST_API_H__
#define __MNIST_TENSOR_RT_MNIST_API_H__

#include <Logger.hh>

#include <NvInfer.h>
#include <NvOnnxParser.h>

#include <map>
#include <memory>
#include <utility>

/**
 * @brief 네트워크 생성 및 해제, 추론을 담당하는 클래스
 */
class MnistApi
{
  private:
    /**
     * @brief TensorRT API에 의해 생성된 오브젝트를 해제하는 deleter
     */
    template <typename T>
    struct _Deleter
    {
        void operator()(T* t)
        {
            t->destroy();
        }
    };

    template <typename T>
    using _Unique = std::unique_ptr<T, _Deleter<T>>;

    template <typename T>
    using _Shared = std::shared_ptr<T>;

  public:
    /**
     * @brief 네트워크 생성 parameter
     */
    struct Param
    {
        /**
         * 모델 파일 경로
         */
        std::string filePath;

        /**
         * 배치 크기
         */
        int batchSize;

        /**
         * 임시 메모리의 최고 크기
         */
        size_t maxMemorySize;

        /**
         * 사용할 정확도
         */
        enum class Precision
        {
            Fp32,
            Fp16,
            Int8,
        } precision
            = Precision::Fp32;

        /**
         * 사용할 DLA 코어 번호
         */
        int idxDlaCore;
    };

  private:
    Logger&                                  _logger;
    std::map<std::string, nvinfer1::Weights> _weightMap;
    _Shared<nvinfer1::ICudaEngine>           _engine;
    Param                                    _param;

  public:
    template <typename ParamT = Param>
    MnistApi(Logger& logger, ParamT&& param)
        : _logger { logger },
          _engine { nullptr },
          _param { std::forward<ParamT>(param) }
    {}

  public:
    /**
     * @brief 네트워크 엔진을 만듭니다.
     */
    bool Build();

    /**
     * @brief 추론합니다.
     */
    bool Infer();

    /**
     * @brief 할당한 자원을 해제합니다.
     */
    bool CleanUp();

  private:
    bool _ConstructNetwork(nvinfer1::IBuilder*           builder,
                           nvinfer1::INetworkDefinition* network,
                           nvinfer1::IBuilderConfig*     config,
                           nvonnxparser::IParser*        parser);

    // https://github.com/NVIDIA/TensorRT/blob/release/7.0/samples/common/common.h#L508
    void _SetAllTensorScales(nvinfer1::INetworkDefinition* network,
                             float                         in,
                             float                         out);

    // https://github.com/NVIDIA/TensorRT/blob/release/7.0/samples/common/common.h#L563
    bool _EnableDla(nvinfer1::IBuilder*       builder,
                    nvinfer1::IBuilderConfig* config,
                    int                       idx_dla_core,
                    bool                      allow_gpu_fallback);

    bool _ValidateNetwork(nvinfer1::INetworkDefinition* network);
};

#endif