import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 21

GPIO.setup(LED, GPIO.OUT)

def blink_led(ledState):
    # print("Blink led")

    while True:
        ledState = not ledState
        GPIO.output(LED, ledState)
        time.sleep(0.5)

def exit():
    # Al termine del codice, facciamo pulizia (reset su tutte le porte/pin utilizzate nel programma)  
    GPIO.cleanup() 

def main(args=None):
    ledState = False

    blink_led(ledState)
    exit()
 
if __name__ == "__main__":
    main()