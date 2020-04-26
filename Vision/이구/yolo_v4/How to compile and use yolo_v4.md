# how to use yolo_v4
> reference: https://github.com/AlexeyAB/darknet

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

3. 사용(webcam)
~~~(bash)
./darknet detector demo ./cfg/coco.data ./cfg/yolov4.cfg ./yolov3.weights -c 0
~~~

<img src="Vision/이구/img/screenshot.png" width="80%" height="80%" title="Vision/이구/img/screenshot.png">

이용하는 사람이 너무 많아서 아직 weights 파일을 다운받을 수 없었다.
