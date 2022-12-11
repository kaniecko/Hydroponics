import time
import RPi.GPIO as GPIO

def get_ph():
    print("getting PH...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(4, GPIO.IN)
    print(GPIO.input(4))
    GPIO.cleanup()

get_ph()
