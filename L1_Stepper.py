#This code rotates a stepper motor a specified theta in degrees
#Designed for 28BYJ-48 stepper motor and ULN-2003 motor driver board
#Uses half step mode for greater precision
#import external libraries
import L1_gpio as gpio
import numpy as np
import time

#define variables
theta = 60          #degrees to rotate
steps = 0           #converted degrees to steps (calculated in StepDegrees)
currentstep = 0     #current step state 0-7 updated by Step Degrees, and returned by step degrees to be stored in main program
gpioport = 1        #gpio port (gpio1 is automatically configured to output on Beaglebone Blue)

#functions
def StepRotate(currentstep, gpioport):    #takes the current step and gpioport and outputs the appropriate stepper values 
    if currentstep == 0:            #0x1: initializes stepper motor but also maintains state
        gpio.write(gpioport,0,1)    #stepper motor driver ULN-2003 operates on 4 bit binary input
        gpio.write(gpioport,1,0)    #stepper motor driver operation in half step: 0x1, 0x3, 0x2, 0x6, 0x4, 0xC, 0x8, 0x9,
        gpio.write(gpioport,2,0)
        gpio.write(gpioport,3,0)
    elif currentstep == 1:          
        gpio.write(gpioport,1,1)    #0x3
    elif currentstep == 2:
        gpio.write(gpioport,0,0)    #0x2
    elif currentstep == 3:
        gpio.write(gpioport,2,1)    #0x6
    elif currentstep == 4:
        gpio.write(gpioport,1,0)    #0x4
    elif currentstep == 5:
        gpio.write(gpioport,3,1)    #0xC
    elif currentstep == 6:
        gpio.write(gpioport,2,0)    #0x8
    elif currentstep == 7:
        gpio.write(gpioport,0,1)    #0x9
    else:
        print("ERROR: invalid current step")
    time.sleep(0.001)    #wait for motor to rotate; approximately 4 second 360 time for 1/64 reduction ratio

def StepDegrees(theta, currentstep, gpioport):    #takes an input theta in degrees, currentstep, gpio port, and rotates the stepper motor that many degrees and returns currentstep
    steps = round(theta/.0879) + 1  #calculates the number of steps+1 to achieve degress (1/64 reduction ratio, 4096 steps for full rotation)
    for i in range(steps):  #loops for number of steps-1
        Steprotate(currentstep, gpioport) #calls steprotate function
        if currentstep == 7:    #updates currentstep and resets current step to 0 if currentstep = 7
            currentstep = 0
        elif currentstep > 7:
            print("ERROR: invalid current step")
        else:
            currentstep = currentstep + 1
    return currentstep
    
#if standalone
while 1:
    currentstep = StepDegrees(theta, currentstep, gpioport)
    time.sleep(1)