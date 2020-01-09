#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
import RPi.GPIO as GPIO

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + msg.data)

def listener():
    rospy.init_node'six_sensors_subscriber', anonymous=True)
    rospy.Subscriber('distance_from_6_sensors',Float32MultiArray, callback)

    rospy.spin()

if __name__=='__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        rospy.loginfo('Measurement stopped by user.')



