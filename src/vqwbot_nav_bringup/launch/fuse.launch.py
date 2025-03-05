# launch file for Fuse
#
# <launch>
#   <param name="/use_sim_time" value="true"/>

#   <node name="state_estimator" pkg="fuse_optimizers" type="fixed_lag_smoother_node">
#     <rosparam command="load" file="$(env HOME)/fuse_tutorials/fuse_simple_tutorial.yaml"/>
#   </node>

#   <node name="bag_play" pkg="rosbag" type="play" args="$(env HOME)/fuse_tutorials/turtlebot3.bag --clock -d 3"/>

#   <node name="rviz" pkg="rviz" type="rviz" args="-d $(env HOME)/fuse_tutorials/fuse_tutorials.rviz"/>
# </launch>

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

    default_fuse_params_path = PathJoinSubstitution([
        FindPackageShare("vqwbot_nav_bringup"),
        "params",
        "fuse_params.yaml"
    ])

    ld = LaunchDescription()
    ld.add_action(launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='False', description='Flag to enable use_sim_time'))
    ld.add_action(launch.actions.DeclareLaunchArgument(name='fuse_params', default_value=default_fuse_params_path, description='Absolute path to [fuse] params file'))
    ld.add_action(launch.actions.DeclareLaunchArgument(name='log_level', default_value='INFO', description='the Logging level'))

    fuse_node = launch_ros.actions.Node(
         package='fuse_optimizers',
         executable='fixed_lag_smoother_node',
         name='fuse_state_estimator_node',
         output='screen',
         arguments=["--ros-args", "--log-level", LaunchConfiguration('log_level')],
         parameters=[ {'load:': LaunchConfiguration('fuse_params')} , {'use_sim_time': LaunchConfiguration('use_sim_time')} ]
    )
    ld.add_action(fuse_node)

    return ld
