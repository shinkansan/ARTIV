# How to use YOLO_mark
Author: 이  구
date: 2020.06.26
> reference: https://github.com/AlexeyAB/Yolo_mark

## Requirements
Opencv 2.X,Opencv 3.X, Opencv 4.X

## Install

```(bash)
git clone https://github.com/AlexeyAB/Yolo_mark
cd Yolo_mark
cmake .
make
```
## Video to Image files
직접 찍은 동영상 파일로부터 이미지 파일을 얻어야 한다.

```(bash)
./yolo_mark x64/Release/data/img cap_video [test.mp4] [10]
```

[test.mp4]의 위치에 이용할 동영상 파일 이름을 넣는다. (webm 형식도 가능)   
[10]은 몇 프레임마다 이미지를 저장할 것인지를 의미한다.

이후, 아래의 코드를 통해 yolo_mark를 실행한다.

```(bash)
./linux_mark.sh
```
## How to use yolo_mark   
**h 키를 누르면 자세한 사용법을 볼 수 있다.**   
1. object id를 선택한다.   
2. 이미지에서 해당 물체가 있는 영역을 드래그하여 직사각형으로 mark한다.   
3. 해당 이미지의 모든 물체를 mark한 후, 스페이스바를 누르면 다음 이미지로 넘어간다.   

  <annotation 하는 법>   
    마우스 왼쪽 버튼을 누른채 드래그 하면 mark 할 수 있다.   
    마우스 오른쪽 버튼을 누른채 이미 그려진 사각형의 위치를 이동할 수 있다.   
    c 키를 누르면 mark한 모든 것들을 지울 수 있다.    


