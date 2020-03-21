# 차량 내부 온도조절하기 part2
김찬영 / 2020. 03. 21

이전 포스팅 : [차량 내부 온도조절하기 part1](./thermal_control_part1.md)   
이후 포스팅 : ~~차량 내부 온도조절하기 part3~~

지난 파트에서 아이오닉 트렁크가 고립계라는 가정하에 IPC를 한 시간동안 작동시키면   
주변 공기가 **3000ºC** 라는 ~~정신나간~~ 온도가 된다는 결과를 얻었다.   
그러나 이는 매우 근사된 계산이기에 더 합당한(?) 예상 결과를 보아야 하고,   
가능한 효율적이면서 효과가 좋은 온도조절 방법을 찾아야 한다.   

그래서 사용하는 것이 유체 시뮬레이션이며,   
Solidworks의 flow simulation 애드온을 사용할 수도 있지만   
현재 Autodesk사의 Inventor를 사용하고 있으므로 동일사의 유체 시뮬레이터인 CFD를 사용한다.

<img src="./media/CFD.jpg" title="CFD.jpg" >

설치 링크는 아래에 있으며, Inventor와 동일하게 대학생 프로모션으로 무료 사용이 가능하다.   
https://www.autodesk.com/education/free-software/cfd-ultimate

**단, 그냥 설치하다간 ~~나처럼~~ 뭐가 문제인지도 모르고 빙글빙글 돌기 마련이니 아래 링크를 참조하라.**

[Autodesk CFD 설치](./CFD_install.md)

## Simulation System 모델링

계산 방법이 정확하다면 계산 대상 또한 정확할수록 그 결과가 의미가 높아진다.   
무슨 말이냐면, LiDAR로 두 진자 사이의 거리를 측정 하는데   
진자운동을 선형 모델로 근사하면 LiDAR의 정확한 측정 능력이 무용지물이 되는거처럼.

그러니까 우리도 Autodesk CFD 라는 정확한 flow simulation tool을 사용하는 만큼,   
열원도, 계(系)도 더 정확하게 모델링할 필요가 있다.   
그렇다고 트렁크 안쪽의 손잡이나 시트의 잔굴곡 등을 다 모델링할 수는 없는 노릇이다.   
이번 글에서는 그 타협점을 잡으면서 Autodesk Inventor로 열원인 IPC와 계(系)인 아이오닉 차량을 모델링한다.


