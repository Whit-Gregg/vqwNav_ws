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

    # ekf_config_path = PathJoinSubstitution([
    #     FindPackageShare('vqwbot_nav_bringup'),
    #     'params',
    #     'ekf.yaml'
    # ])
    
    ukf_config_path = PathJoinSubstitution([
        FindPackageShare('vqwbot_nav_bringup'),
        'params',
        'ukf.yaml'
    ])
    
    # xacro_urdf_file_path = PathJoinSubstitution([
    #     FindPackageShare('vqwbot_nav_bringup'),
    #     'urdf',
    #     'vqwbot.urdf.xacro'
    # ])

    # default_rviz_config_path = PathJoinSubstitution([
    #     FindPackageShare("vqwbot_nav_bringup"),
    #     "params",
    #     "nav2_default_view.rviz"
    # ])

    default_nav2_params_path = PathJoinSubstitution([
        FindPackageShare("vqwbot_nav_bringup"),
        "params",
        "nav2_params.yaml"
    ])

    default_nav2_map_path = PathJoinSubstitution([
        FindPackageShare("vqwbot_nav_bringup"),
        "map",
        "nav2_map.yaml"
    ])

    #  /opt/ros/jazzy/share/nav2_bt_navigator/behavior_trees
    #   nav2_bt_navigator/navigate_to_pose_w_replanning_goal_patience_and_recovery.xml

#[component_container_isolated-2] [ERROR] [2024-12-11 10:47:51.189] [bt_navigator] Couldn't open input XML file: nav2_bt_navigator/behavior_trees/navigate_to_pose_w_replanning_goal_patience_and_recovery.xml
#[component_container_isolated-2] [ERROR] [2024-12-11 10:47:51.189] [bt_navigator] Error loading XML file: nav2_bt_navigator/behavior_trees/navigate_to_pose_w_replanning_goal_patience_and_recovery.xml

    
    # robot_description =  {'robot_description': Command(['xacro ', LaunchConfiguration('model')])}

    ld = LaunchDescription()
    # ld.add_action(launch.actions.DeclareLaunchArgument(name='model', default_value=xacro_urdf_file_path, description='Absolute path to robot urdf xarco file'))
    # ld.add_action(launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path, description='Absolute path to rviz config file'))
    ld.add_action(launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='False', description='Flag to enable use_sim_time'))
    ld.add_action(launch.actions.DeclareLaunchArgument(name='nav2_params', default_value=default_nav2_params_path, description='Absolute path to nav2 params file'))
    ld.add_action(launch.actions.DeclareLaunchArgument(name='map', default_value=default_nav2_map_path, description='Absolute path to nav2 map file'))

    # robot_localization_node = launch_ros.actions.Node(
    #      package='robot_localization',
    #      executable='ukf_node',
    #      name='ukf_filter_node',
    #      output='screen',
    #      parameters=[ ukf_config_path , {'use_sim_time': LaunchConfiguration('use_sim_time')} ]
    # )
    # ld.add_action(robot_localization_node)

    slam_toolbox_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        [os.path.join(get_package_share_directory('slam_toolbox'), 'launch', 'online_async_launch.py')])
    )
    ld.add_action(slam_toolbox_launch)

    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'bringup_launch.py')),
        launch_arguments={
            'params_file': LaunchConfiguration('nav2_params'),
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'slam': 'False',
            'map': LaunchConfiguration('map'),
            }.items(),
         )

    ld.add_action(navigation_launch)

    # rviz_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(
    #     [os.path.join(get_package_share_directory('vqwbot_nav_bringup'), 'launch', 'rviz.launch.py')])
    # )
    # ld.add_action(rviz_launch)

    return ld
