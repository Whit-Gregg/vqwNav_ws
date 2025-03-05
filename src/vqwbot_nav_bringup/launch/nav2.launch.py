import os
import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    
    default_nav2_params_path = PathJoinSubstitution([
        FindPackageShare("vqwbot_nav_bringup"),
        "params",
        "nav2_params.yaml"
    ])

    # default_nav2_map_path = PathJoinSubstitution([
    #     FindPackageShare("vqwbot_nav_bringup"),
    #     "map",
    #     "nav2_map.yaml"
    # ])
    default_nav2_map_path = "~/vqwNav_ws/map/nav2_map.yaml"


    ld = LaunchDescription()
    ld.add_action(launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='False', description='Flag to enable use_sim_time'))
    ld.add_action(launch.actions.DeclareLaunchArgument(name='nav2_params', default_value=default_nav2_params_path, description='Absolute path to Nav2 params file'))
    ld.add_action(launch.actions.DeclareLaunchArgument(name='map', default_value=default_nav2_map_path, description='Absolute path to Nav2 map file'))
    ld.add_action(launch.actions.DeclareLaunchArgument(name='log_level', default_value='INFO', description='the Logging level (defaulr = INFO)'))


    # slam_toolbox_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join(get_package_share_directory('vqwbot_nav_bringup'), 'launch', 'slam_toolbox.launch.py')),
    #     launch_arguments={
    #         'use_sim_time': LaunchConfiguration('use_sim_time'),
    #         ##'use_lifecycle_manager': 'True',
    #         }.items(),
    # )
    # ld.add_action(slam_toolbox_launch)


    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'bringup_launch.py')),
        launch_arguments={
            'params_file': LaunchConfiguration('nav2_params'),
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'slam': 'False',
            'use_localization': 'False',
            'map': LaunchConfiguration('map'),
            }.items(),
         )
    ld.add_action(navigation_launch)

    # # ## some other package should be publishing this...????
    # # static_transform_map_to_scan =  launch_ros.actions.Node(
    # #      package='tf2_ros',
    # #      executable='static_transform_publisher',
    # #      name='static_transform_map_to_scan_node',
    # #      output='both',
    # #      arguments=[
    # #                 "--frame-id", "map",
    # #                 "--child-frame-id", "scan", 
    # #                 "--x","0", 
    # #                 "--y", "0",
    # #                 "--z", "0",
    # #                 "--roll" "0",
    # #                 "--pitch", "0",
    # #                 "--yaw", "0",
    # #                  ##"--ros-args", "--log-level", LaunchConfiguration('log_level')
    # #                  ],
    # # )
    # # ld.add_action(static_transform_map_to_scan)


    return ld
