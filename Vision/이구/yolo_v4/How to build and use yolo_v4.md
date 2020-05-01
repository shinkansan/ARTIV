# how to use yolo_v4
> reference: https://github.com/AlexeyAB/darknet

### darknet 빌드

1. 다운
~~~(bash)
mkdir yolo_v4
cd yolo_v4
git clone https://github.com/AlexeyAB/darknet.git
~~~

2. 빌드
~~~(bash)
cd darknet/
mkdir build-release
cd build-release/
cmake ..
make
make install
~~~

### yolo_v4

~~~(bash)
./darknet detector demo ./cfg/coco.data ./cfg/yolov4.cfg ./yolov4.weights -c 0
~~~

yolov4.weights파일은 아래 링크에서 다운받을 수 있다.
https://drive.google.com/uc?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT&export=download

![screenshot](/Vision/이구/img/screenshot.png)

이용하는 사람이 너무 많아서 아직 weights 파일을 다운받을 수 없었다.

![yolo_v4_test](/Vision/이구/img/yolo_v4_test.PNG)

돌려본 결과, 4~6 frame정도 나온다.

makefile CUDA,cudnn, opencv


