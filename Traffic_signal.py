import time
import RPi.GPIO as GPIO
R1 = 3
Y1 = 5
G1 = 7

R2 = 8
Y2 = 10
G2 = 12

R3 = 11
Y3 = 13
G3 = 15

R4 = 32
Y4 = 29
G4 = 31

RUNNING=True

lane1= int(input("Delay_lane1:"))
print(lane1)

lane2= int(input("Delay_lane2:"))
print(lane2)

lane3= int(input("Delay_lane3:"))
print(lane3)

lane4= int(input("Delay_lane4:"))
print(lane4)


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False);


GPIO.setup(R1, GPIO.OUT)

GPIO.setup(Y1, GPIO.OUT)

GPIO.setup(G1, GPIO.OUT)



GPIO.setup(R2, GPIO.OUT)

GPIO.setup(Y2, GPIO.OUT)
                 
GPIO.setup(G2, GPIO.OUT)



GPIO.setup(R3, GPIO.OUT)

GPIO.setup(Y3, GPIO.OUT)

GPIO.setup(G3, GPIO.OUT)



GPIO.setup(R4, GPIO.OUT)

GPIO.setup(Y4, GPIO.OUT)

GPIO.setup(G4, GPIO.OUT)


# Define a function to control the traffic light

def trafficState1(red1, yellow1, green1):

    GPIO.output(R1, red1)

    GPIO.output(Y1, yellow1)

    GPIO.output(G1, green1)



def trafficState2(red2, yellow2, green2):

    GPIO.output(R2, red2)

    GPIO.output(Y2, yellow2)

    GPIO.output(G2, green2)



def trafficState3(red3, yellow3, green3):

    GPIO.output(R3, red3)

    GPIO.output(Y3, yellow3)

    GPIO.output(G3, green3)



def trafficState4(red4, yellow4, green4):

    GPIO.output(R4, red4)

    GPIO.output(Y4, yellow4)

    GPIO.output(G4, green4)

 

print ("Traffic Light Simulation. Press CTRL + C to quit")



# Main loop

try:

    while RUNNING:

        
        print("Green Light ON for Lane 1 ")
        
        trafficState1(0,0,1)

        trafficState2(1,0,0)

        trafficState3(1,0,0)

        trafficState4(1,0,0)

        time.sleep(lane1)

        trafficState1(0,1,0)

        trafficState2(1,0,0)

        trafficState3(1,0,0)

        trafficState4(1,0,0)

        time.sleep(5)

        print("Green Light ON for Lane 2")
        
        trafficState1(1,0,0)

        trafficState2(0,0,1)

        trafficState3(1,0,0)

        trafficState4(1,0,0)

        time.sleep(lane2)

        trafficState1(1,0,0)

        trafficState2(0,1,0)

        trafficState3(1,0,0)

        trafficState4(1,0,0)

        time.sleep(5)


        print("Green Light ON for Lane 3")
        trafficState1(1,0,0)

        trafficState2(1,0,0)

        trafficState3(0,0,1)

        trafficState4(1,0,0)

        time.sleep(lane3)

        trafficState1(1,0,0)

        trafficState2(1,0,0)

        trafficState3(0,1,0)

        trafficState4(1,0,0)

        time.sleep(5)
       
        print("Green Light ON for Lane 4")
        trafficState1(1,0,0)

        trafficState2(1,0,0)

        trafficState3(1,0,0)

        trafficState4(0,0,1)

        time.sleep(lane4)

        trafficState1(1,0,0)

        trafficState2(1,0,0)

        trafficState3(1,0,0)

        trafficState4(0,1,0)

        time.sleep(5)

# If CTRL+C is pressed the main loop is broken

except KeyboardInterrupt:

    RUNNING = False

    print("\Quitting")

 
# Actions under 'finally' will always be called

finally:

    # Stop and finish cleanly so the pins

    # are available to be used again

    GPIO.cleanup()
