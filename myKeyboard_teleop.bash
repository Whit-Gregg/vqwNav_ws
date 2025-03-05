#!/bin/bash
# This script is used to launch the keyboard for the vqwNav project

###ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=diffbot_base_controller/cmd_vel_teleop -p stamped:=true

ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=cmd_vel_teleop -p stamped:=true
