#ifndef __MNIST_TENSOR_RT_LOGGER_H__
#define __MNIST_TENSOR_RT_LOGGER_H__

#include <NvInfer.h>

#include <iostream>

/**
 * 추론을 위해선 ILogger 인터페이스를 구현한 클래스의 인스턴스가 반드시
 * 필요합니다.
 * https://docs.nvidia.com/deeplearning/sdk/tensorrt-developer-guide/index.html#initialize_library
 */
class Logger : public nvinfer1::ILogger
{
  private:
    /**
     * @brief 주어진 severity에 맞는 문자열을 반환합니다.
     */
    static char const* _GetStringFromSeverity(Severity severity);

  private:
    Severity      _threshold;
    std::ostream& _out;

  public:
    Severity threashold()
    {
        return _threshold;
    }

  public:
    /**
     * @param threshold - 출력하지 않을 로그 severity 기준
     * @param out - 출력할 스트림
     */
    Logger(Severity threshold, std::ostream& out)
        : _threshold { threshold }, _out { out }
    {}

  public:
    /**
     * @param severity - 로그의 severity
     * @param msg - 로그 메시지
     */
    virtual void log(Severity severity, char const* msg) override;
};

#endif