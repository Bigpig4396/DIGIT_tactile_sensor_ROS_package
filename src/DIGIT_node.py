#!/usr/bin/env python3
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from digit_interface import Digit

if __name__ == '__main__':
    rospy.init_node('DIGIT_node', anonymous=True)
    pub = rospy.Publisher('DIGIT_frames', Image, queue_size=10)
    d = Digit("D00002")  # replace it with your own serial number, check it with instruction 'digits = DigitHandler.list_digits()' in python
    d.connect()
    bridge = CvBridge()
    r = rospy.Rate(30) # 30hz
    while not rospy.is_shutdown():
        frame = d.get_frame()
        imgMsg = bridge.cv2_to_imgmsg(frame, "bgr8")
        pub.publish(imgMsg)
        r.sleep()
