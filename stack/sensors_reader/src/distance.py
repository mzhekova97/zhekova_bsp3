#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

def distance(trigger,echo):

    PIN_TRIGGER = trigger
    PIN_ECHO = echo

    GPIO.output(PIN_TRIGGER, True)
    
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER,False)

    startTime = time.time()
    stopTime = time.time()

    while GPIO.input(PIN_ECHO)==0:
        startTime = time.time()

    while GPIO.input(PIN_ECHO)==1:
        stopTime = time.time()

    duration = stopTime - startTime

    dist = (duration * 34300)/2 
    
    return dist



