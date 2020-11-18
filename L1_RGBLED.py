#This code Sends out a binary signal to an Arduino running an RGB LED library
#import external libraries
import L1_gpio as gpio

#define variables
State = 0;
gpioport = 0;   #gpio port 0 needs to be configured to output on Beaglebone

#functions
def LEDState(State, gpioport):      #takes the current step and gpioport and outputs the appropriate stepper values 
    if state == 1:                  #Seeking state            
        gpio.write(gpioport, 0, 1)
        gpio.write(gpioport, 1, 0)
        gpio.write(gpioport, 2, 0)
        gpio.write(gpioport, 3, 0)
    elif state == 2:                #Firing state
        gpio.write(gpioport, 0, 0)
        gpio.write(gpioport, 1, 1)
        gpio.write(gpioport, 2, 0)
        gpio.write(gpioport, 3, 0)
    elif state == 3:                #Error State
        gpio.write(gpioport, 0, 0)
        gpio.write(gpioport, 1, 0)
        gpio.write(gpioport, 2, 1)
        gpio.write(gpioport, 3, 0)
    elif state == 4:                #Manual Control State
        gpio.write(gpioport, 0, 0)
        gpio.write(gpioport, 1, 0)
        gpio.write(gpioport, 2, 0)
        gpio.write(gpioport, 3, 1)
    else:
        print("ERROR: TURTL State not valid")