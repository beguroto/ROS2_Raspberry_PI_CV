import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# GPIOs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
#          12, 13, 16, 17, 18, 19, 20, 21,
#          22, 23, 24, 25, 26, 27]

GPIOsOut = [17,23,24,27]

GPIO.cleanup()

# Setup all GPIOsOut to output
for gpio in GPIOsOut:
    GPIO.setup(gpio, GPIO.OUT)

try:  
    while True:  
        for gpio in GPIOsOut:
            GPIO.output(gpio, 1)
            sleep(1.5)  

        # Read state for each GPIOsOut
        for gpio in GPIOsOut:
            print("GPIO no " + str(gpio) + ": " + str(GPIO.input(gpio)))

        for gpio in GPIOsOut:
            GPIO.output(gpio, 0)
            sleep(1.5)  

        # Read state for each GPIOsOut
        for gpio in GPIOsOut:
            print("GPIO no " + str(gpio) + ": " + str(GPIO.input(gpio)))
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup() 
    
