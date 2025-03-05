#!/bin/bash

cd ./src/vqwbot_nav_bringup
source install/setup.bash

# ros2 launch vqwbot_nav_bringup nav2.launch.py

ros2 launch vqwbot_nav_bringup full.launch.py

