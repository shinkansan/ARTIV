# Making Packaging in ROS2
Making packaing in ROS2 is like insatll program into your computer.   


## Install Colcon build dependency
`sudo apt install python3-colcon-common-extensions`

* 다른 디펜던시를 make 했다면 알 것이다. 보통 cmake를 쓰는데, 여기서는 colcon을 쓴다. ros2와 친해서.. (참고로 ros1은 catkin을 쓰는데 명령어는 검색해보자, 이것도 많이 쓴다. 대부분의 ros 관련 오픈소스가 catkin으로 작성되어있다.)
물론 cmakefile은 규격을 따라서 cmake로도 된다!.

## C++ Version
  ROS의 컴파일 시스템은 workspace라는 개념이 있는데 아래와 같은 구조에서 만드는 것이다. 그래서 폴더명을 보통 ros1 용 ws면 ros1_ws, 2면 ros2_ws 라고한다. 혹은 colcon_ws, catkin_ws 라고도 많이 한다.
  

  1. First we have to make workspace which source code placed and builded in (for first time only)
    `mkdir -p ~/dev_ws/src`   
    `cd ~/dev_ws/src`   
    `ros2 pkg create --build-type ament_cmake <package_name>`      
    보통 패키지를 만들고 안에 src에 cpp를 그냥 만들어줘도 된다.
    
   우리는 아래 파라미터로 cpp를 하나 만들어 놓으면 초반 cmakefile을 생성해줘서 편해서 아래 명령어로 진행한다.
       
   In this Tutorial we use `ros2 pkg create --build-type ament_cmake --node-name my_node my_package`
   And Colcon build hierachy is `package > node`   
    
   > Visual Studio로 치면 my_node는 일종의 cpp 파일이고, my_package는 project 이름이다. 
    
   Then, folder looks like below   
    
    dev_ws/ 
      src/
        my_package/   
            CMakeLists.txt   
            package.xml   
              src/   
                my_node.cpp
         
 나중에 같은 패키지안에 cpp 파일을 추가하고 싶으면 그 패키지 src안에 그냥 cpp 를 추가하고 cmakelist에 cpp를 추가하면 된다.
 
 다른 프로젝트를 만드는 것은 위의 명령어 또 하면되고.
                
   2. And you can write your code in 'my_node.cpp'
   __Example__
   ```C++
   #include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, char ** argv)
{
  (void) argc;
  (void) argv;

  printf("hello world my_package package\n");

  cout << "Hello World" << endl;
  
  int _tempInteger{0};
  for(;;){
    if (_tempInteger > 101) break;
    cout << _tempInteger << endl;
    _tempInteger++;
  }
  return 0;
}
```
3. Build it!
  Goto ~/dev_ws
  and `colcon build`
  
4. Source it!   
> 이 소스는 왜 사용하냐면요! 컴파일이 된 실행 파일을 ros2 run [패키지이름] [노드이름] 으로 실행 할 수 있어요.   
> 보통 상식상으로 컴파일 되면 윈도우는 .exe 파일이 생성되는데 Linux 계열은 그렇게 안되거든요 직접 실행하는 방법은 ws안에 build 폴더안에서   
> 그냥 실행 파일을 이름을 터미널에 치면되고요!

우리는 ros2 용 패키지를 만든거니까, 빌드한 프로그램을 ros2 패키지로 등록하는 절차라고 보시면 됩니다.

  Inside dev_ws
  
  여튼 dev_ws안에서는    
  `source insatll/setup.bash`
  >  __절대경로가 아닙니다.__ , 절대 경로로도 할 수 있어요, 이경우에 보통 ws를 홈 폴더에 넣으니 `source ~/dev_ws/install/setup.bash` 하면 되겠죠? (리눅스에서 ~/ 이뜻은 Home 폴더를 뜻하는 것입니다.)

5. Run it   
  `ros2 run my_pakcage my_node`
  
## Python
    1. First we have to make workspace which source code placed and builded in (for first time only)
    `mkdir -p ~/dev_ws/src`   
    `cd ~/dev_ws/src`   
    `ros2 pkg create --build-type ament_python <package_name>`   
    In this Tutorial we use `ros2 pkg create --build-type ament_python --node-name my_node_python my_package_python`
    And Colcon build hierachy is `package > node`
    
   Then, folder looks like below   
    
    dev_ws/ 
      src/
        my_package_python/   
          setup.py
          package.xml   
              my_package_python/   
                my_node_python.py
                
   2. And you can write your code in 'my_node_python.py'
   __Example__
   ```C++
   def main():
    print('Hi from my_package_python.')
    i = 0
    while(True):
        if i > 101: break
        print(i)
        i = i+1;


if __name__ == '__main__':
    main()
```
3. Build it!
  Goto ~/dev_ws
  and `colcon build`
  
4. Source it!
  Inside dev_ws
  `source install/setup.bash`

5. Run it   
  `ros2 run my_pakcage_python my_node_python`
   
   
## 3. Customize Install Setting

  cpp package 만들면서 생성되는 CMAKE 관련해서는 다음 챕터 publisher package 만들기에 상세하게 적혀있습니다!!

  두개를 보통 설정하는데, pkg create 명령어 하는 경우에는 상황에 자동생성되서 신경 안써도되긴 합니다.
  
  1. Package.xml
    description and license contain TODO notes. 
    __AND Depencies Link__ 
    
  2.setup.py (python only)
    description and license contain TODO notes. 
    __NOTICE : You need to match information same as Package.xml__
  
  
## Next
Make Publisher for seonsor input
    
     


