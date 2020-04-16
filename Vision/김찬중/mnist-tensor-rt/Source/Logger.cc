#include <Logger.hh>

using nvinfer1::ILogger;

char const* Logger::_GetStringFromSeverity(ILogger::Severity severity)
{
    switch (severity)
    {
    case Severity::kINTERNAL_ERROR: return "[INTERNAL ERROR]";
    case Severity::kERROR: return "[ERROR]";
    case Severity::kWARNING: return "[WARNING]";
    case Severity::kINFO: return "[INFO]";
    case Severity::kVERBOSE:
    default: return "[VERBOSE]";
    }
}

void Logger::log(ILogger::Severity severity, char const* msg)
{
    // 기준보다 심각성이 심하지 않은 로그는 무시
    if (static_cast<int>(severity) > static_cast<int>(_threshold))
        return;

    _out << _GetStringFromSeverity(severity) << ' ' << msg << std::endl;
}