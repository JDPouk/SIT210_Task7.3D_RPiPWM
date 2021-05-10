import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import random
from time import sleep  # Importing sleep from time library

led_pin = 23            # Initializing the GPIO pin 23 for LED

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(led_pin, GPIO.OUT)   # Declaring pin 21 as output pin

pwm = GPIO.PWM(led_pin, 100)    # Created a PWM object
pwm.start(0)                    # Started PWM at 0% duty cycle

def distance():
    dist = random.randrange(1,4)
    if dist == 4:s
        s_close = random.ranrange(75,100)
        return s_close
    if dist == 3:
        close = random.randrange(50,75)
        return close
    if dist == 2:
        far = random.randrange(25,50)
        return far
    if dist == 1:
        s_far = random.randrange(0,25)
        return s_far

try:
    while 1:
       x = distance()
       pwm.ChangeDutyCycle(x) # Change duty cycle
       sleep(1)         # Delay of 1 sec
            

# If keyboard Interrupt (CTRL-C) is pressed
except KeyboardInterrupt:
    pass        # Go to next line

pwm.stop()      # Stop the PWM
GPIO.cleanup()  # Make all the output pins LOW