// 프로그램의 엔트리 포인트

#include <Logger.hh>
#include <MnistApi.hh>

#include <NvInfer.h>
#include <NvOnnxParser.h>

#include <iostream>

using namespace std;
using nvinfer1::ILogger;

int main(int argc, char** argv)
{
    Logger   logger { ILogger::Severity::kINFO, cout };
    MnistApi api {
        logger,
        MnistApi::Param {
            "model.onnx",
            1,
            16 * 1024 * 1024,
            MnistApi::Param::Precision::Fp16,
            0,
        },
    };

    if (!api.Build())
        return 1;

    if (!api.Infer())
        return 2;

    if (!api.CleanUp())
        return 3;

    return 0;
}