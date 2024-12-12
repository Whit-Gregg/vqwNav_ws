#!/bin/bash

# Execute the colcon command
colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTING=OFF
