# rostopic delay and the Solution of delay

* 'ros topic의 지연여부를 알려면 어떤 방식을 사용해야 될까?'라는 주제에 대한 매뉴얼입니다! 

  ##

  ### 1. rostopic에 내장된 `rostopic delay`

  사용방법 : `$ rostopic delay /topic_name`
  
  기능 : 헤더가 있는 주제에 대한 지연을 표시합니다.
  

  ##
  ### 2. 활용예제 : ROS Image subscriber delay
  
  상황 설명 : 5Hz로 /camera/image_raw로 이미지를 스트리밍하는 rosbag 사용, 
            
             참조를 위해 이미지를 display하는 image_view 노드 (5Hz로 display),
             
             (image_view 노드와 지연시간을 비교하기 위한 이미지를 display) rospy subscriber 
             
             (initialized with queue = 1)
             
             
