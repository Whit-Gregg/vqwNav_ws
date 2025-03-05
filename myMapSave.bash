#!/bin/bash

# bash function that returns a string containing the date and time formatted as YYYY-MM-DD_HH-MM-SS


#!/bin/bash

# bash function that returns a string containing the date and time formatted as YYYY-MM-DD_HH-MM-SS
get_current_datetime() {
    echo $(date +"%Y-%02m-%02d_%02H-%02M-%02S")
}


map_file_name=~/vqwNav_ws/map/nav2_map__asof_$(get_current_datetime)

slam_map_file_name=~/vqwNav_ws/map/slamtoolbox_map__asof_$(get_current_datetime)
slam_map_common_file_name=~/vqwNav_ws/map/slamtoolbox_map

echo "Saving map to file: $map_file_name"
ros2 run nav2_map_server map_saver_cli -f $map_file_name

ros2 service call /slam_toolbox/serialize_map slam_toolbox/SerializePoseGraph "{filename: $slam_map_file_name}"

ros2 service call /slam_toolbox/serialize_map slam_toolbox/SerializePoseGraph "{filename: $slam_map_common_file_name}"
