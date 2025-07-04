cmake_minimum_required(VERSION 3.0.2)
project(self_checkout_system)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  sensor_msgs
  cv_bridge
  sound_play
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
  PROGRAMS
    nodes/yolo_detect_node.py
    nodes/checkout_logic_node.py
    nodes/tts_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY
  launch
  models
  webapp
  scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# Uncomment if you have configs later
# install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
