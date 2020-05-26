### Made by Seunggi Lee
### 항속주행 + PID control

PID control이 정확히 작동하는지 확인해 볼 필요 있음.  
ROS2에서 작동하기 때문에 dbw_ioniq_node를 사용해 속도를 받아와도 되지만, 데이터의 양이 커서 그냥 JointState로 속도값을 받아옴.
Angular speed control 하려면 아마 dbw_ioniq_node 사용해야 할듯?  

visualization.py은 현재 속도를 matplotlib으로 시각화 해주는 파일, desired speed(cruise speed)도 같이 출력하도록 수정해야 함.

# TODO
> - 오르막길에서 accel 값이 늦게 들어가고, 내리막길에서 브레이크가 늦게 들어감.
> - 오르막길에서 accel 값이 늦게 들어가는 건 Anti wind-up을 어느정도 늘리면 해결될 것으로 생각됨.
> - 내리막길에서 brake 값이 늦게 들어가는 건 brake의 데드존을 조정함으로써 해결 가능할 것으로 보임.??
> - Settling time이 체감상 길었음.
> - Version 1.0 에서는 계수를 각각 P = 1.25, I = 0.75, D = 0, windup_gaurd = 70으로 사용하였음.
> - D제어기 사용을 안했었으므로 추후 D제어기 계수 조정 필요 -> overshoot이 해결될 것 같음.
> - 추후 동영상 촬영, 시각화, rosbag으로 기록할 필요 있음.
> 
> - 0527) kp = 1.25, ki = 0.9, kd = 0.1로 했을 때 평지에서 desired speed가 15이면, overshoot이 25정도로 나오고 settling time이 상당히 길다.  
> - 가장 문제점: overshoot이 너무 크고, settling time이 너무 길다.  
