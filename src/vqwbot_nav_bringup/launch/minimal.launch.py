import os
import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # xacro_urdf_file_path = PathJoinSubstitution([
    #     FindPackageShare('vqwbot_bringup'),
    #     'urdf',
    #     'vqwbot.urdf.xacro'
    # ])

    # robot_description =  {'robot_description': Command(['xacro ', LaunchConfiguration('model')])}

    # robot_controllers_path = PathJoinSubstitution([
    #     FindPackageShare("vqwbot_bringup"),
    #     "params",
    #     "roboclaw_controllers.yaml"
    # ])

    # ros2_control_node = Node(
    #     package="controller_manager",
    #     executable="ros2_control_node",
    #     parameters=[robot_description, robot_controllers_path],
    #     output="both",
    # )
    # robot_state_pub_node = Node(
    #     package="robot_state_publisher",
    #     executable="robot_state_publisher",
    #     parameters=[robot_description],
    #     remappings=[],
    #     output="both",
    # )

    # joint_state_broadcaster_spawner = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    #     output="both",
    # )

    # robot_controller_spawner = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["diffbot_base_controller", "--controller-manager", "/controller_manager"],
    #     output="both",
    # )


    nodes = [
        # launch.actions.DeclareLaunchArgument(name='model', default_value=xacro_urdf_file_path, description='Absolute path to robot urdf xarco file'),
        # ros2_control_node,
        # robot_state_pub_node,
        # joint_state_broadcaster_spawner,
        # robot_controller_spawner,
    ]

    return LaunchDescription(nodes)
