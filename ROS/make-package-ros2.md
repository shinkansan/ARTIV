# Making Packaing in ROS2
Making packaing in ROS2 is like insatll program into your computer.   


## Install Colcon build dependency
`sudo apt install python3-colcon-common-extensions`


## C++ Version
  1. First we have to make workspace which source code placed and builded in (for first time only)
    `mkdir -p ~/dev_ws/src`   
    `cd ~/dev_ws/src`   
    `ros2 pkg create --build-type ament_cmake <package_name>`   
    In this Tutorial we use `ros2 pkg create --build-type ament_cmake --node-name my_node my_package`
    And Colcon build hierachy is `package > node`
    
   Then, folder looks like below   
    
    dev_ws/ 
      src/
        my_package/   
            CMakeLists.txt   
            package.xml   
              src/   
                my_node.cpp
                
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
  Inside dev_ws
  `source insatll/setup.bash`

5. Run it   
  `ros2 run my_pakcage my_node`
  
## Python
    1. First we have to make workspace which source code placed and builded in (for first time only)
    `mkdir -p ~/dev_ws/src`   
    `cd ~/dev_ws/src`   
    `ros2 pkg create --build-type ament_python <package_name>`   
    In this Tutorial we use `ros2 pkg create --build-type ament_python --node-name my_node my_package`
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
  `source insatll/setup.bash`

5. Run it   
  `ros2 run my_pakcage_python my_node_python`
   
    
    
     


