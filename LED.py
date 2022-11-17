import RPi.GPIO as GPIO
import time
led1Pin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led1Pin, GPIO.OUT)

while True:
    print("on")
    GPIO.output(led1Pin, True)
    time.sleep(0.1)
    
    print ("off")
    GPIO.output(led1Pin, False)
    time.sleep(0.1)
    

   
    




