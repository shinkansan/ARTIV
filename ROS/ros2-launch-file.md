# ROS2 Launch file

[Link](https://index.ros.org/doc/ros2/Tutorials/Launch-Files/Creating-Launch-Files/)

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='image_sub_cpp',
            #node_namespace='image_sub_cpp',
            node_executable='ros2_image_sub_cpp',
            node_name='sub_image_sample'
        ),
        Node(
            package='image_sub_py',
            
            node_executable='image_sub_py',
            node_name='image_sub_py'
        ),
        Node(
            package='speed_pub_cpp',
            node_executable='speed_pub_cpp',
            node_name='speed_ms_echo',
        )
    ])
```




## What is ROS nodelet
https://answers.ros.org/question/230972/what-is-a-nodelet/


