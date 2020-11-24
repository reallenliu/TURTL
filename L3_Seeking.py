# Import external libraries
import numpy as np
import time
import math

# Import internal programs
import L2_shoot as shoot
import L2_color_target as ct
import L2_kinematics as kin
import L2_speed_control as sc
import L2_inverse_kinematics as inv
import L2_log as log
import L2_vector as vec
import L2_obstacle as obstacle
import L1_lidar as lidar
import L1_RGBLED as rgb
# initialize variables for control system
t0 = 0
t1 = 1
e00 = 0
e0 = 0
e1 = 0
dt = 0
de_dt = np.zeros(2)  # initialize the de_dt
count = 0

# initialize variables for color tracking
color_range = np.array([[165, 130, 130], [220, 220, 220]])  # Input your HSV choices
thetaOffset = 0  # the measured offset of target (degrees)
x = 0  # target center location (pixels)

# initialize variables for seeking and movement
myThetaDot = 0
Target = 0
target_theta = 0
acq_target =[]
currentstep = 0

# Function to rotate/drive SCUTTLE (copied from lab7 template)
def Move(myXdot, myThetaDot):
    A = np.array([myXdot, myThetaDot])
    pdTargets = inv.convert(A)  # convert from [xd, td] to [pdl, pdr]
    kin.getPdCurrent()  # capture latest phi dots & update global var
    pdCurrents = kin.pdCurrents  # assign the global variable value to a local var
    global t0
    global t1
    global e00
    global e0
    global e1
    global dt
    global de_dt

    # UPDATES VARS FOR CONTROL SYSTEM
    t0 = t1  # assign t0
    t1 = time.time()  # generate current time
    dt = t1 - t0  # calculate dt
    e00 = e0  # assign previous previous error
    e0 = e1  # assign previous error
    e1 = pdCurrents - pdTargets  # calculate the latest error
    de_dt = (e1 - e0) / dt  # calculate derivative of error

    # CALLS THE CONTROL SYSTEM TO ACTION
    sc.driveClosedLoop(pdTargets, pdCurrents, de_dt)  # call the control system
    # sc.driveOpenLoop(pdTargets)  # call the control system
    time.sleep(0.005)  # very small delay.

def isNone():
    global acq_target
    if acq_target is None:
        acq_target = np.array([0,0,0])
        
# Function for scanning and identifying a target
def ColorScan():
    global acq_target
    global myThetaDot
    global target_theta
    # acq_target should be holding an array
    acq_target = ct.colorTarget()
    isNone()

    while acq_target[0] is None:                       # if a NoneType is returned, print "no target found"
        print("No Target Found")
        Move(0, -.79)                               # rotate to the right
        acq_target = ct.colorTarget()               # search for a target again
        isNone()
    Move(0,0)
    
    target_theta = ct.horizLoc(acq_target[0])       # the estimated angle to the identified target
    print("Angle to target: ", target_theta)

    if target_theta > 3:                            # if object is to the right, rotate right at x rad/s
         myThetaDot = .15

    elif target_theta < -3:                         # if object is to the left, rotate left at -x rad/s
         myThetaDot = -0.15

def Center():
    global target_theta
    while target_theta != 0:                        # continue rotating until the target is centered
        ColorScan()
        Move(0, myThetaDot)
        ColorScan()
        target_theta = ct.horizLoc(acq_target[0]) # update target_theta
    Move(0, 0)                                      # stop rotating after target_theta == 0

# function for driving to target once SCUTTLE is centered
def Approach():
    tar_vals = vec.getTarget()                      # get valid distances and angles for the middle 6 of 108 readings
    avg_dist = np.average(tar_vals[:,0])            # get the average of the distances
    print("Distance to target: ", avg_dist)
    print("Approaching Target")
    # target is already a centered so move forward with a constant velocity
    while avg_dist > 1:                            # while the distance to the target is greater than 1 ft
        Center()
        Move(.15,0)                                  # move forward at .2m/s
        tar_vals = vec.getTarget()
        avg_dist = np.average(tar_vals[:, 0])       # update the distance to the target
    Move(0,0)                                       # stop all movement


# infinite while loop
while (1):
    currentstep
    ColorScan()                                     # first identify the target
    Approach()                                      # approach the scuttle
    Move(0,0)
    currentstep = shoot.fire(1,1,currentstep)
    Move(0,0)
    ColorScan()
   # shoot.fire(1,1, currentstep)
    

    
#RUN BEFORE EVERYTHING: bash start_mjpg_streamer.sh L3_image_filter.py