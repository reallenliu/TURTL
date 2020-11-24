# Lab4Template.py
# Team Number: 3
# Hardware TM: Noah Gomez
# Software TM: Jonathan Guyton
# Date: 09.30.20
# Code purpose: Get and Display PDL, PDR, xdot, and thetadot

# Import Internal Programs
import L2_kinematics as kin
import L2_heading as head
import L2_log as log

# Import External programs
import numpy as np
import time

# DEFINE THE FUNCTIONS FOR THE PROGRAM
def task2():
    x = kin.getMotion()                             # obatining values from getMotion() function in L2_kinematics
    print ("xdot(m/s), thetadot (rad/s):", x)       #printing xdot and thetadot
    log.uniqueFile(x[0], "xdot.txt")                #logging xdot
    log.uniqueFile(x[1], "thetadot.txt")            #logging thetadot
    y = kin.getPdCurrent()                          #obatining values from getPDCurrents() function in L2_kinematics
    log.uniqueFile(y[0], "PDL.txt")                 #logging PDL
    log.uniqueFile(y[1], "PDR.txt")                 #logging PDR
    print ("PDL, PDR: ", y)                         #printing PDL and PDR values
   
    axes =  head.getXY()                            #call xy function
    axesScaled = head.scale(axes)                   #perform scale function
    h = head.getHeading(axesScaled)                 #compute the heading
    headingDegrees = round(h*180/np.pi, 2)          #coverting to degrees
    log.uniqueFile(headingDegrees, "Heading.txt")   #logging heading
    print ("Heading: ", headingDegrees)             #print headinging

# UNCOMMENT THE LOOP BELOW TO RUN THE PROGRAM CONTINUOUSLY
while 1:
    task2()                                         # calling task2 function
    time.sleep(0.2) # delay a short period
    