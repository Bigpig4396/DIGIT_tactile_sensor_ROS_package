# DIGIT_tactile_sensor_ROS_package

ROS package of sensor DIGIT

Lambeta, Mike, et al. "Digit: A novel design for a low-cost compact high-resolution tactile sensor with application to in-hand manipulation." IEEE Robotics and Automation Letters 5.3 (2020): 3838-3845.

publish at topic "DIGIT_frames" at 30 Hz, read it as an image sequence.

file "DIGIT_node.py" is the interface of DIGIT and ROS, user should replace the sensor serial number with their owns. file "DIGIT_plot_node.py" is an example file that read data from topic "DIGIT_frames" and plot them in OpenCV.

Depedencies:
OpenCV-python
Facebook DIGIT interface
https://github.com/facebookresearch/digit-interface
