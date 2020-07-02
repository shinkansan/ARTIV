# TestCase

Author : Juho Song

v1 : 2020.06.29. [/v1](https://github.com/shinkansan/ARTIV/blob/master/integraedSW/VANGUARD%20(Self-Diagnosis%20protocol)/TestCase/TestCase(v1).py)

v2 : 2020.07.01. [/v2](https://github.com/shinkansan/ARTIV/blob/master/integraedSW/VANGUARD%20(Self-Diagnosis%20protocol)/TestCase/TestCase(v2).py)

v3 : 2020.07.02. [/v3](https://github.com/shinkansan/ARTIV/blob/master/integraedSW/VANGUARD%20(Self-Diagnosis%20protocol)/TestCase/TestCase(v3).py)

plotting : 2020.07.02. [/confidence_interval](https://github.com/shinkansan/ARTIV/blob/master/integraedSW/VANGUARD%20(Self-Diagnosis%20protocol)/TestCase/confidence_interval.py)

##

* 초깃값 진단의 기준이 될 신뢰성 높은 차량 정보 Dataset을 확보한다.
* VANGUARD의 기능 중 차량 정보에 해당하는 부분을 간접적으로 모두 담고 있어, VANGUARD의 모체가 된다.

![BPS_ACT_Feedback TestCase](https://user-images.githubusercontent.com/59792475/86363993-94827680-bcb2-11ea-83f9-386a1edf9338.png)

![BPS_Feed TestCase](https://user-images.githubusercontent.com/59792475/86364006-99472a80-bcb2-11ea-8f8f-fa87bf1637c1.png)

실제 브레이크에 사용되는 액츄에이터값인 BPS Feed 값을 이용하여 브레이크 엑츄에이터의 상태를 사전에 점검한다.

##

> **TODO**   
> 1. current 첫값이 time.time()에 해당하는 값이 직접 들어오는 현상 (2020.06.30 해결)
> 2. break가 한 번 pub 되면 정상궤도로 돌아오지 않고 계속 최댓값으로 유지되는 현상 (2020.07.01 해결)
> 3. multiprocessing의 Process를 쓰면 코드가 돌아가지 않는 현상
> 4. real-time plotting 해보기
