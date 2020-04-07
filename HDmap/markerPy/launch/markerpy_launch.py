from launch import LaunchDescription
from launch_ros.actions import Node
import launch
def generate_launch_description():
    
    return LaunchDescription([
        Node(
            package='markerPy',
            node_executable='markerPy',
	),

        Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            args='6720409 12574038 0 0 0 0 1 map osmMap',
            node_name='speed_ms_echo',
        )
    ])
