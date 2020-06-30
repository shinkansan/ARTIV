# TestCase

* __초깃값 진단의 기준이 될 신뢰성 높은 차량 정보 Dataset을 확보한다.__
* __VANGUARD의 기능 중 차량 정보에 해당하는 부분을 간접적으로 모두 담고 있어, VANGUARD의 모체가 된다.__

<p align="center">Author : Juho Song</p>
<p align="center">date : 2020.06.29.(v1)</p>
<p align="center">date : 2020.07.01.(v1)</p>

해결해야 할 이슈

### 1. current 첫값이 time.time()에 해당하는 값이 직접 들어오는 현상 (2020.06.30 해결)

2. break가 한 번 pub 되면 정상궤도로 돌아오지 않고 계속 최댓값으로 유지되는 현상 (2020.07.01 해결)

3. multiprocessing의 Process를 쓰면 코드가 돌아가지 않는 현상

4. real-time plotting 해보기
