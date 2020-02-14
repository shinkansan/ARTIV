# 0. 시작
Author : 이 구</br>
Date : 2020.02.14.

### 컴퓨터 비전이란?
말 그대로, 기계의 시각에 해당하는 부분을 연구한다. 자율주행차에서 컴퓨터 비전은 카메라를 통해 입력되는 영상에서 차선 인식, 객체 인식 등을 수행한다. 
 
### 그런데 카메라는?
문제가 있다. 우리는 말 그대로 **처음**부터 자율주행차를 만들고, 당연히 카메라도 없다. **어떤** 카메라를 **몇 개** 써야할까?
아무것도 모르는 상태로, 대략적인 기준을 생각해보았다.
  
    1. 약 30FPS 이상?
    2. 적당한 화질?
    3. 카메라가 360도를 보도록?
  
카메라가 360도를 보도록 하려면 몇 개의 카메라가 필요한지 알아보기 위해 스펙을 살펴봤지만 FOV에 관한 정보는 찾아볼 수 없었고, 스펙표의 항목들이 무엇을 의미하는지도 몰랐다.<br/>
알고보니, FOV는 렌즈에 따라 달라졌다. 지금 생각해보면 당연한거지만, 정말 몰랐다. 싸구려 웹캠만 써오다가 진짜 카메라를 쓰려니 신경써야 할게 한두가지가 아니다.<br/>

다음 링크의 글을 한번 읽어보면, 스펙표의 항목들이 무엇을 의미하는지 대충은 알 수 있다. 
[링크](https://www.baslerweb.com/ko/vision-campus/vision-systems-and-components/find-the-right-lens/)

### 렌즈 찾기
카메라가 360도를 볼 수 있도록, 적당한 렌즈를 찾아보았다. 예산이 한정되어 있고, 여유롭지 않으니 최대한 적은 수의 카메라를 쓸 수 있도록 수평 FOV가 최대한 넓은 렌즈를 찾아보았다.<br/><br/>

그렇게 찾은게 [이거](https://www.aico-lens.com/product/5mm-10mp-manual-iris-wide-angle-4k-c-mount-lens-ach0518m10m/)다. 수평 FOV 82.7도로, 카메라를 4개 달면 330도까지 볼 수 있다.

**나중에 알았는데, FOV와 해상도에 trade-off가 있다고 한다... 다시 찾아보자.**

### 찾은 카메라, 렌즈 목록
카메라
1. FLIR Grasshopper3 USB3 [링크](https://www.flir.com/products/grasshopper3-usb3?model=GS3-U3-15S5C-C)
2. FLIR Blackfly S USB3 [링크](https://www.flir.eu/products/blackfly-s-usb3/?model=BFS-U3-50S5C-C)

렌즈
1. ACH0518M10M [링크](https://www.aico-lens.com/product/5mm-10mp-manual-iris-wide-angle-4k-c-mount-lens-ach0518m10m/)<br/>
~~2. 수평 FOV 좁은 렌즈도 찾기~~
