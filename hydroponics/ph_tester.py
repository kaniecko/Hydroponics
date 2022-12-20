import time
import RPi.GPIO as GPIO

def get_ph():
    pin_number = 16
    print("getting PH...")
    GPIO.setmode(GPIO.BOARD)
    print("after setupmode")
    GPIO.setup(pin_number, GPIO.IN)#, pull_up_down=GPIO.PUD_UP)
    print("after setup pin IN")
    print(GPIO.input(pin_number))
    GPIO.cleanup()
    print("...Done")

get_ph()
