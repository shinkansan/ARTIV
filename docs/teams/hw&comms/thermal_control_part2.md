# 차량 내부 온도조절하기 part2
2020/03/21 김찬영

[차량 내부 온도조절하기 part1](./thermal_control_part1.md)

지난 파트에서 아이오닉 트렁크가 고립계라는 가정하에 IPC를 한 시간동안 작동시키면   
주변 공기가 3000ºC 라는 ~~정신나간~~ 온도가 된다는 결과를 얻었다.   
그러나 이는 매우 근사된 계산이기에 더 합당한(?) 예상 결과를 보아야 하고,   
가능한 효율적이면서 효과가 좋은 온도조절 방법을 찾아야 한다.   

그래서 사용하는 것이 유체 시뮬레이션이며,   
Solidworks의 flow simulation을 사용할 수도 있지만   
현재 Autodesk사의 Inventor를 사용하고 있으므로 동일사의 유체 시뮬레이터인 CFD를 사용한다.

<img src="./media/CFD.jpg" title="CFD.jpg" >

설치 링크는 아래에 있으며, Inventor와 동일하게 대학생 프로모션으로 무료 사용이 가능하다.   
https://www.autodesk.com/education/free-software/cfd-ultimate

단, 평소 하던대로 설치하다간 ~~나처럼~~ 뭐가 문제인지도 모르고 빙글빙글 돌기 마련이니 아래 방법에 따라 설치하자.

## Autodesk CFD 설치

