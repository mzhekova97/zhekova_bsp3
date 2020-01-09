#!/usr/bin/env python
import rospy
import distance
from std_msgs.msg import Float32MultiArray 
import RPi.GPIO as GPIO

def talker():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD) # mode--> pin

    #Sensor 1 - front:
    trig1=15
    echo1=32
    first=(trig1,echo1)

    #Sensor 2 - bottom:
    trig1=33
    echo1=11
    second=(trig2,echo2)

    #Sensor 3 - back right:
    trig3=16
    echo3=18
    third=(trig3,echo3)

    #Sensor 4 - top:
    trig4= 22
    echo4= 39
    fourth=(trig4,echo4)

    #Sensor 5 - front right:
    trig5=31
    echo5=32
    fift=(trig5,echo5)

    #Sensor 6 - front left:
    trig6=7
    echo6=35
    sixth=(trig6,echo6)

    dataset=(first,second,third,fourth,fifth,sixth)

    pub = rospy.Publisher('distance_from_6_sensors',Float32MultiArray, queue_size=10)
    rospy.init_node('sensor_reader', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():    
        measures = []
        for i in dataset:
            x=list(i)
            GPIO.setup(x[0], GPIO.OUT)
            GPIO.setup(x[1], GPIO.IN)
            dist=str(round(distance.distance(x[0],x[1]),2))
            measures.append(dist)
            
        mes=Float32MultiArray(data=measures)
        print(mes.data)
        rospy.loginfo(mes)
        pub.publish(mes)
        rate.sleep()
    GPIO.cleanup()


if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.loginfo('Measurement stopped by user.')"""
