""" This script controls cooling fan for Raspberry Pi

Following is hardware setup

                 +5V DC ____
                         |
                         |
                    _+ve_|______
                    | 5 V      |
                    | BLDC FAN |
                    | 200 mA   |
                    |__________|
                     -ve |
                   | |---'
                   | |<--,
       GPIO 12  ___| |___|
                     |
                     |
                     ~ GND
"""

from time import sleep
from subprocess import check_output
from re import findall

import RPi.GPIO as GPIO


def get_temp():
    """ Returns core temperature in float - deg C """
    temp = check_output(['vcgencmd', 'measure_temp']).decode('UTF-8')
    temp = float(findall('\d+\.\d+', temp)[0])
    return temp


# GPIO to use for control
IOPIN = 12

# Temperature settings
MINTEMP = 50
MAXTEMP = 55

# Delay time in seconds
DELAY = 5

# GPIO mode is board, thus pin number can be called to identify pin
GPIO.setmode(GPIO.BOARD)

# Set pin 12 as output
GPIO.setup(IOPIN, GPIO.OUT)

try:
    while True:
        """ Get temperature, and Turn on fan if greater than max temp
        turn off if less than min temp. Max temp != min temp to
        add hysterisis """

        TEMP = get_temp()

        if TEMP > MAXTEMP:
            GPIO.output(IOPIN, True)

        elif TEMP < MINTEMP:
            GPIO.output(IOPIN, False)

        sleep(DELAY)

except Exception:
    # Clean exit to release GPIO
    GPIO.cleanup()
