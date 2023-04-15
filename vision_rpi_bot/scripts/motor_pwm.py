import RPi.GPIO as GPIO
import time

#Pin gestione motori
right_motor_a = 23
right_motor_b = 24
right_motor_en = 25

left_motor_a = 14
left_motor_b = 15
left_motor_en = 16


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)