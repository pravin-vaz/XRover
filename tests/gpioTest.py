#! /usr/bin/python3
# gpioTest.py is to test GPIO pins on Raspberry Pi 

import RPi.GPIO as GPIO
import time

#  set GPIO modes
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)

#  set GPIO pin mode
GPIO.setup (17, GPIO.OUT)
GPIO.setup (22, GPIO.OUT)
GPIO.setup (23, GPIO.OUT)
GPIO.setup (24, GPIO.OUT)

#  turn motors off
GPIO.output(17,0)
GPIO.output(22,0)
GPIO.output(23,0)
GPIO.output(24,0)

#  turn right motor forward
GPIO.output(17,0)
GPIO.output(22,1)

#  turn left motor forward
GPIO.output(23,0)
GPIO.output(24,1)

time.sleep(1)

#  Reset GPIO and turn off motors
GPIO.cleanup()