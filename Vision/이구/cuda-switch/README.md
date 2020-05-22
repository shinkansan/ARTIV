# How can use different CUDA version in same machine
Author : 이  구 <br/>
 > reference: https://github.com/phohenecker/switch-cuda

## Use
~~~bash
$ git clone https://github.com/phohenecker/switch-cuda
$ cd switch-cuda
~~~

1. 설치되어 있는 모든 CUDA version 확인   
~~~bash
source switch-cuda.sh
~~~

2. 특정 버전의 CUDA 선택   
~~~bash
source switch-cuda.sh 10.0
~~~

*****source한 터미널에만 적용된다.*****
