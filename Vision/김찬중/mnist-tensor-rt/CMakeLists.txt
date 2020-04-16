cmake_minimum_required(VERSION 3.15)
project(mnist-tensor-rt)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(CUDAToolkit REQUIRED)

add_executable(${PROJECT_NAME}
    ${PROJECT_SOURCE_DIR}/Source/Logger.cc
    ${PROJECT_SOURCE_DIR}/Source/Main.cc
    ${PROJECT_SOURCE_DIR}/Source/MnistApi.cc
)
target_include_directories(${PROJECT_NAME}
    PUBLIC ${PROJECT_SOURCE_DIR}/Include
)
target_link_libraries(${PROJECT_NAME}
    CUDA::cudart
    CUDA::cublas
    CUDA::nvrtc
    cudnn
    rt
    nvinfer
    nvinfer_plugin
    nvonnxparser
    nvparsers
)