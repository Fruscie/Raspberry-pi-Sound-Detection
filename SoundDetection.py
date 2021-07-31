#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
soundPin1 = 4
soundPin2 = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(soundPin1, GPIO.IN)
GPIO.setup(soundPin2, GPIO.IN)
def callback(channel):
        print(channel)
        if channel == soundPin1:
            print ("Sound1 Detected!")
        elif channel == soundPin2:
            print ("Sound2 Detected!")

GPIO.add_event_detect(soundPin1, GPIO.RISING,callback=callback, bouncetime=300)  # let us know when the pin goes HIGH or LOW
# GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
GPIO.add_event_detect(soundPin2, GPIO.RISING,callback=callback, bouncetime=300)
# infinite loop
while True:
        time.sleep(1)