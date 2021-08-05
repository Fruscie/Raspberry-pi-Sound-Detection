import RPi.GPIO as GPIO
import time

#GPIO SETUP
soundPin = 26
led = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(soundPin, GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(led,GPIO.OUT)
def callbacks(argument):
        print(argument)
        if GPIO.input(soundPin) == 1:
            print("Sound Detected! = " +str(GPIO.input(soundPin)))
#             GPIO.output(led,HIGH)
        elif GPIO.input(soundPin) == 0:
            print("Sound Detected! fall = " +str(GPIO.input(soundPin)))
        else:         
            print("No Sound Detected!")
#             GPIO.output(led,LOW)
GPIO.add_event_detect(soundPin, GPIO.RISING,callback=callbacks, bouncetime=300)  # let us know when the pin goes HIGH or LOW
# GPIO.add_event_callback(sound, callback)  # assign function to GPIO PIN, Run function on change

# # infinite loop
# while True:
#     print('Im doing something')
#     time.sleep(300)
#     print('baru')

