# rostopic delay and the Solution of delay

* 'ros topic의 지연여부를 알려면 어떤 방식을 사용해야 될까?'라는 주제에 대한 매뉴얼입니다! 

  ##

  ### 1. rostopic에 내장된 `rostopic delay`

  사용방법 : `$ rostopic delay /topic_name`
  
  기능 : 헤더가 있는 주제에 대한 지연을 표시합니다.
  

  ##
  ### 2. 활용예제 : ROS Image subscriber delay
  
  __개요 :__
  
             5Hz로 /camera/image_raw로 이미지를 스트리밍하는 rosbag 사용, 
            
             참조를 위해 이미지를 display하는 image_view 노드 사용 (5Hz로 display),
             
             (image_view 노드와 지연시간을 비교하기 위한 이미지를 display) rospy subscriber 
             
             (initialized with queue = 1)
             
  __예상 결과 :__
            
             queue 크기가 1이므로 subscriber는 최신 프레임을 처리하고 그 동안 다른 모든 프레임을 건너 뛰어야한다. 
            
             처리가 완료되면, 오래된 프레임을 queue에 넣지 않고, 다음 최신 프레임으로 이동해야한다.
             
             이로 인해, 고르지는 않지만 lag이 없는 비디오가 생성되어야 함.(fps가 낮지만 rosbag stream delay가 없는)
             
 
  __실제 결과 :__
            
             published stream 뒤에 subscriber가 지연된다. 
            
             구체적으로, image_view 노드는 이미지를 5Hz로 표시하며 subscriber가 최신 이미지를 가져 오는 대신,
             
             모든 이미지를 대기열에 놓고 하나씩 처리하는 것으로 보인다.
             
             또한, delay가 시간이 지남에 따라 증가한다.
             
             rosbag stream을 중지해도, subscriber는 queue가 1임에도 queue의 이미지를 계속 처리한다.
            
  __naive solution :__
            
             subscriber의 버퍼를 매우 크게 설정하면, 앞의 예상 결과 대로 실행된다.
             
   `self.subscriber = rospy.Subscriber("/camera/image_raw", Image, self.callback, queue_size = 1, buff_size=2**24)`
 
 
 __fundamental solution :__
            
             버퍼 솔루션은 clean하지 않다.
             
             image_view 노드는 cv_bridge + opencv와 더불어 많은 리소스를 사용하기에 이미지 자체를 지연시키는 경향이 있고,
             
             그렇기에 topic stream에서의 Delay를 계산하려는 접근 자체가 잘못되었다.
             
             publisher가 ros transport hint를 변경하지 않는다면, 서로 다른 2개의 노드에서 image topic을 
             
             subscribing 한 후에도 노드가 불안정하다. 
             
             해결 방법은, subscriber nodes를 멈추고 이미지가 정확하게 스트리밍 되는지(특히나 코드에서) 확인하고,
             
             `rostopic delay someTopic`을 사용하여 delay를 확인하는 것이다.
             
             문제가 여전히 지속된다면, publisher의 transport_hint를 UDP로 변경해본다.
             
             (real driver에서는 가능한데, rosbag에서는 힘듬)
             
 __additional solution :__
            
             image나 point clouds와 같은 대형 messages로 작업 할 때, `nodelet` 사용을 추천한다. 아래 링크 첨부
             
__[ros wiki nodelt](http://wiki.ros.org/nodelet)__
             
__[nodelet 한글자료](https://blog.naver.com/PostView.nhn?blogId=rich0812&logNo=221466635955&categoryNo=0&parentCategoryNo=0)__
            
            
             
             
             
  
             
