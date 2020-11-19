#This code Sends out a binary signal to an Arduino running an RGB LED library
#import external libraries
import L1_gpio as gpio

#define variables
State = 0
gpioport = 0  #gpio port 0 needs to be configured to output on Beaglebone

#functions
def LEDState(State, gpioport):      #takes the current step and gpioport and outputs the appropriate stepper values 
    if state == 1:                  #Seeking state            
        gpio.write(gpioport, 0, 0)
        gpio.write(gpioport, 1, 0)
        gpio.write(gpioport, 2, 0)
    elif state == 2:                #Found Target
        gpio.write(gpioport, 0, 0)
        gpio.write(gpioport, 1, 0)
        gpio.write(gpioport, 2, 1)
    elif state == 3:                #Shooting target
        gpio.write(gpioport, 0, 0)
        gpio.write(gpioport, 1, 1)
        gpio.write(gpioport, 2, 1)
    elif state == 4:                #Turning Left
        gpio.write(gpioport, 0, 0)
        gpio.write(gpioport, 1, 1)
        gpio.write(gpioport, 2, 1)
    elif state == 5:                #Turning Right
        gpio.write(gpioport, 0, 1)
        gpio.write(gpioport, 1, 0)
        gpio.write(gpioport, 2, 0)
    elif state == 6:                #Mission Complete
        gpio.write(gpioport, 0, 1)
        gpio.write(gpioport, 1, 0)
        gpio.write(gpioport, 2, 1)
    elif state == 7:                #Failure
        gpio.write(gpioport, 0, 1)
        gpio.write(gpioport, 1, 1)
        gpio.write(gpioport, 2, 0)
    elif state == 8:                #Manual Control Mode
        gpio.write(gpioport, 0, 1)
        gpio.write(gpioport, 1, 1)
        gpio.write(gpioport, 2, 1)
    else:
        print("ERROR: TURTL State not valid")
