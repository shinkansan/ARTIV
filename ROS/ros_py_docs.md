# ROS [rclpy, rclcpp] 디펜던시 설명


이 사이트를 요약/해석한 내용입니다. 

- 파이썬 버전 [링크](http://docs.ros2.org/latest/api/rclpy/api/init_shutdown.html)
- CPP 버전 [링크](http://docs.ros2.org/latest/api/rclcpp/)


이제 패키지를 만들줄도 알고 Pub, Sub도 얼추 만들 수 있다고 생각합니다. _흑흑_   
처음에 예제코드를 베끼고, 인터넷 검색을 통해 하나하나 넣어봤을텐데요!


이제는 각 의미가 무엇인지 알아보고 어떤 종류가 있는지 알아봅시다.

잠깐! 여기 써 있는건 아주아주 기초적인거고, 상세내용은 위의 링크를 클릭해주세요, 뭐가 있는지랑 이 디펜던시가 뭐가 가능한지를 알아야 
나중에 검색해서라도 찾을 수 있게 읽어보시길 바랍니다. 심심하면 여기에 추가해도되요!


## ROS 노드 만드는 4단계
  1. Initialization (초기화)
  2. Create one or more ROS nodes (최소 한개의 ROS 노드 만들기)
  3. Process node callbacks (콜백 만들기, 그냥 코드짜기)
  4. Shutdown (노드가 종료되었을때 뒷자리도 깔끔해야한다.)
  
  __1. 초기화__   
   > Inititalization is done by calling init() for a particular Context. __This must be done before any ROS nodes can be created.__
   노드 만들기전에 초기화 (초기설정) 을 해줘야 한다.
  관련 코드 
  #### `rclpy.init(*, args=None, context=None)`   
  Initialize ROS communications for a given context.
  
  __Parameters__   
    1. args (Optional[List[str]]) – List of command line arguments.   
    2. context (Optional[Context]) – The context to initialize. If None, then the default context is used (see get_default_context()).   
    
  __2. 최소 한개의 ROS 노드 만들기__   
   > Creating a ROS node is done by calling create_node() or by instantiating a Node. A node can be used to create common ROS entities like publishers, subscriptions, services, and actions.
   
  관련 코드 
  ```
  rclpy.create_node(node_name, *, context=None, cli_args=None, namespace=None, use_global_arguments=True, start_parameter_services=True, parameter_overrides=None, allow_undeclared_parameters=False, automatically_declare_parameters_from_overrides=False)   
  Create an instance of Node.
  
  Parameters : 

     node_name (str) – A name to give to the node. 노드이름, ROS에서 이걸로 구분한다. 보통 이것만 설정

     context (Context) – The context to associated with the node, or None for the default global context.

     cli_args (List[str]) – Command line arguments to be used by the node. Being specific to a ROS node, an implicit –ros-args scope flag always precedes these arguments.

     namespace (str) – The namespace prefix to apply to entities associated with the node (node name, topics, etc).

     use_global_arguments (bool) – False if the node should ignore process-wide command line arguments.

     start_parameter_services (bool) – False if the node should not create parameter services.

     parameter_overrides (List[Parameter]) – A list of Parameter which are used to override the
                      initial values of parameters declared on this node.

     param allow_undeclared_parameters –
            if True undeclared parameters are allowed, default False. This option doesn’t affect parameter_overrides.

     automatically_declare_parameters_from_overrides (bool) – If True, the “parameter overrides” will be used to implicitly declare parameters on the node during creation, default False.

    Return type
        Node

    Returns
        An instance of the newly created node. 
 ```
    
    
  
  
