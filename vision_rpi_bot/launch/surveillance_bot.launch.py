import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions


def generate_launch_description():
    os.system("export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp")
    
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='vision_rpi_bot', executable='image_publisher_rgb_node', name='ai_bot',
            output= 'screen',
            ),
    ])