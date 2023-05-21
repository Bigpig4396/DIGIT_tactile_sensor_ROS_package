#!/usr/bin/env python3
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from digit_interface import Digit
import cv2

def callback(data):
    orig = bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.imshow('image', orig)
    cv2.waitKey(20)


if __name__ == '__main__':
    rospy.init_node('DIGIT_plot_node', anonymous=True)
    rospy.Subscriber("DIGIT_frames", Image, callback)
    bridge = CvBridge()
    rospy.spin()
