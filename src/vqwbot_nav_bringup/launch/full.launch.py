from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    nav2_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        [os.path.join(get_package_share_directory('vqwbot_nav_bringup'), 'launch', 'navigation.launch.py')])
    )
    ld.add_action(nav2_launch)

    slam_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        [os.path.join(get_package_share_directory('vqwbot_nav_bringup'), 'launch', 'slam_toolbox.launch.py')])
    )
    ld.add_action(slam_launch)

    return ld
