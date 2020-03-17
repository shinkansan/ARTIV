# 모델 성능 향상

여기서는 모델을 향상하기 위한 다양한 방법을 배웁니다.


### 학습 단계
기본적으로 학습 후에는 모델을 탑재하여 원하는 서비스를 해야되는데요, 보통 파이썬을 트레이닝에 사용했으니, 추론에도 사용하는게 
개발자 입장에서는 편합니다. 이미 파이썬으로 제작했기도 해서 손이 많이 익히기도 했죠

하지만

#### Python Bottleneck
일반적으로 사용하는 CPython은 GIL으로 인해 Multi-threading 성능에 제약이 생깁니다. 또한, Python의 GC 때문에 Response Time이 크게 튀는 경우가 존재합니다. Production 환경에서 Flask 등과 같은 Python 웹서버를 통해 서비스한다면, Request Throughput 및 GC 로 인해 가끔 지나치게 느린 것이 문제가 될 수 있습니다.

TensorFlow는 TensorFlow Serving을 통해 Serving 할 수 있습니다.
PyTorch는 TorchScript 및 libTorch 를 통해 모델을 Jit Compile 하고, C++ 환경에서 Serving 할 수 있습니다.
대부분 딥러닝 모델 학습시에 PyTorch를 사용하고, 이를 TensorFlow(>= 2.0)로 변환하여 TensorFlow Serving을 통해 Serving하고 있습니다. TensorFlow 가 2.0으로 업데이트되면서 PyTorch와 거의 똑같은 코드로 모델을 변환할 수 있고, TensorFlow Serving이 gRPC 와 ProtoBuf 를 지원하여 PyTorch에 비해 서비스 환경을 최적화하는데 유리하기 때문입니다.

#### 병렬 처리   
ㅍ수학관련 라이브러리인, MKL 등을 이용하면 빠른 연산이 가능합니다 거기다가 병렬연산 처리도 한다면? 굉장히 좋은 효과를 기대할 수 있습니다.
병렬처리를 위한 환경변수 설정
병렬처리를 위해 사용하는 양대산맥인 OpenMP와 TBB의 환경변수를 적절히 설정하는 것만으로도 큰 성능 향상을 기대할 수 있습니다.

아래와 같은 변수 설정으로 10~15%의 성능 향상을 얻었습니다.

```bash
CORES=`lscpu | grep Core | awk '{print $4}'`
SOCKETS=`lscpu | grep Socket | awk '{print $2}'`
TOTAL_CORES=`expr $CORES \* $SOCKETS`

KMP_SETTING="KMP_AFFINITY=granularity=fine,compact,1,0"
KMP_BLOCKTIME=1

export OMP_NUM_THREADS=$TOTAL_CORES
export $KMP_SETTING
export KMP_BLOCKTIME=$KMP_BLOCKTIME

echo -e "### using OMP_NUM_THREADS=$TOTAL_CORES"
echo -e "### using $KMP_SETTING"
echo -e "### using KMP_BLOCKTIME=$KMP_BLOCKTIME\n"
```
`bashrc`에 넣어서 동작합니다.

모델과 환경에 따라 최적화된 옵션은 다를 수 있으므로, OpenMP* Implementation-Defined Behaviors 및 Linking with Threading Libraries 를 참고하셔서 실험을 통해 결정하시면 코드 변경 없이 만족할만한 성능 향상을 기대할 수 있을 것이라 생각합니다.


### 모델 경량화

모델도 만들다 보면 다른 데이터 구조처럼, 압축도할 수 있고, 필요없는 부분을 처내서 몸무게 감량도 할 수 있는데요,
처리하는 데이터량이 줄어드니 당연히 속도도 향상되겠죠? 반면에 정확도는 최대한 유지하는게 관건입니다. 이미 학계에서는 많은 기술이 나왔는데요

![사진](https://blog.pingpong.us/images/2020.03.11.ml-model-optimize/pruning-quantization-distillation.png)
출처 :핑퐁팀 블로그 

1. 중요하지 않은 부분을 적절히 가지치기를 해서 줄일 것이냐 (Pruning)
2. 해상도를 낮춰서 작게 만들 것이냐 (Quantization)
3. 사이즈 자체를 작게 만들 것이냐 (Distillation)


Pruning과 Quantization은 아래를 참고하시면 도움이 될 것 입니다.

  TensorFlow는 NVIDIA 에서 제공하는 SDK인 TensorRT를 이용하여 경량화할 수 있습니다.
  TrtGraphConverter
  PyTorch는 NVIDIA 에서 제공하는 APEX를 이용하여 경량화할 수 있습니다.
  단, APEX를 사용하시면 주의하실 것들이 있습니다.
  
  PyTorch 버전이 1.3.1 이어야 합니다. 1.3.0 버전은 버그가 있어서 FP16 연산이 지원되지 않습니다.
  PyTorch 바이너리를 빌드한 CUDA 버전과 로컬 머신의 CUDA 버전이 소숫점 한 개까지 일치해야합니다.
  PyTorch 1.3.1이 10.1 버전으로 빌드되었으므로, 반드시 CUDA 10.1 버전을 사용하여야 합니다.
  Pip 19.3.1 버전에 버그가 있으므로, Pip 19.0 버전으로 다운그레이드하여 설치해야합니다.
