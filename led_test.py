#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

num = 0

while 10 >= num:
	print('O N')
	GPIO.output(11, True)
	time.sleep(1)
	print('OFF')
	GPIO.output(11, False)
	time.sleep(1)
	num += 1
