### Made by Seunggi Lee
### 항속주행 + PID control

PID control이 정확히 작동하는지 확인해 볼 필요 있음.
ROS2에서 작동하기 때문에 dbw_ioniq_node를 사용해 속도를 받아와도 되지만, 데이터의 양이 커서 그냥 JointState로 속도값을 받아옴.

# TODO
> - 오르막길에서 accel 값이 늦게 들어가고, 내리막길에서 브레이크가 늦게 들어감.
> - 오르막길에서 accel 값이 늦게 들어가는 건 Anti wind-up을 어느정도 늘리면 해결될 것으로 생각됨.
> - 내리막길에서 brake 값이 늦게 들어가는 건 brake의 데드존을 조정함으로써 해결 가능할 것으로 보임.??
> - Settling time이 체감상 길었음.
> - Version 1.0 에서는 계수를 각각 P = 1.25, I = 0.75, D = 0, windup_gaurd = 70으로 사용하였음.
> - D제어기 사용을 안했었으므로 추후 D제어기 계수 조정 필요 -> overshoot이 해결될 것 같음.
> - 추후 동영상 촬영, 시각화, rosbag으로 기록할 필요 있음.
