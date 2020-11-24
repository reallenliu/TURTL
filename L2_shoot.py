#imports
import numpy as np
import time 
import L1_motors as motors
import L1_Stepper as stepper

currentstep = 0

#this function loads a ball and then fires 
def fire(m1,m2,currentstep):
    print("loading")
    motors.accy(m1,3)
    motors.accy(m2,4)
    time.sleep(.5)
    currentstep = stepper.StepDegrees(60,currentstep,1)
    print("Firing")
    time.sleep(4.5)
    motors.accy(0,3)
    motors.accy(0,4)
    return currentstep
 
#while(1):
 #   currentstep = fire(1,1,currentstep)
  #  time.sleep(1)

    
 