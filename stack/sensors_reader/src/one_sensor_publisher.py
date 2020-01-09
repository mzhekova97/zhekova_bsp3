#!/usr/bin/env python
import rospy
import distance
from std_msgs.msg import Float32
import RPi.GPIO as GPIO

def talker():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD) # mode--> pin

    #front sensor:
    trig=15
    echo=32
    
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    pub = rospy.Publisher('distance_from_1_sensor',Float32, queue_size=10)
    rospy.init_node('sensor_reader', anonymous=True)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        dist=distance.distance(trig,echo)
        rospy.loginfo(dist)
        pub.publish(dist)
        rate.sleep()

    GPIO.cleanup()


if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.loginfo('Measurement stopped by user.')

	
	




