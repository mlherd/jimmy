# ros_jimmy

Wiki Page
- https://github.com/mlherd/ros_jimmy/wiki

Hardware:
- USB2Dynamixel
- Powerhub
- 12V Power Supply
- HROS5

Pre-Install:
- Operating System: Linux Ubuntu 14.04
- ROS Distribution: ROS Indigo
- Make sure dynamixel_controllers package is successfully installed
- Make sure USB port is available/accessible.
- Make sure id numbers and servo limits (min, max) are same as in the motor.yaml
- http://wiki.ros.org/dynamixel_controllers

Install Steps:
- cd catkin_ws/src
- download the git repository
- cd ..
- source devel/setup.bash
- catkin_make
- make sure there are no error messages
- open a terminal and type
- cd catkin_ws
- source devel/setup.bash

Testing
- roslaunch jimmy jimmy.launch
- make sure there are no error messages. If there are yellow and red colored lines run the lunch file again.
- Select an option. Make sure you are in the keyboard window when you select an option.

Topics
- Subscribed Topics
- /play_motion (std_msgs/String)
- Motion file name. For example:
- rostopic pub -1 /play_motion std_msgs/String stand

Portland State University - Intelligent Robotics Lab - email: herdogan@pdx.edu
