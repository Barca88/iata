from time import sleep

## import math, signal, sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# initialise variables
delayTime = 0.5

# Input pin for the digital signal will be picked here
Digital_PIN = 24
GPIO.setup(Digital_PIN, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

try:
    while True:
        print(GPIO.input(Digital_PIN))

        sleep(delayTime)



except KeyboardInterrupt:
    GPIO.cleanup()
