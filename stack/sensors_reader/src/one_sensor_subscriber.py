#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import RPi.GPIO as GPIO

def callback(msg):
    rospy.loginfo(str(msg.data))

def listener():
    rospy.init_node('one_sensor_subscriber', anonymous=True)
    rospy.Subscriber('distance_from_1_sensor',Float32, callback)

    rospy.spin()

if __name__=='__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        rospy.loginfo('Measurement stopped by user.')
