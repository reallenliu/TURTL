# Lab6 Task 3
# Team Number: 3
# Hardware TM: Noah Gomez
# Software TM: Jonathan Guyton
# Date: 10.21.20
# Code purpose: Get and Display PDL, PDR, xdot, and thetadot

# Import Internal Programs
import L2_vector as vec
import L2_log as log
import time 
import math                                     # importing math to use sin and cos

while 1:
    Plot = vec.getNearest();
    Distance = Plot[0];
    Angle = Plot[1];
    Dy = Distance*math.sin(Angle);              #Dy is the variable for the disance in the Y direction.
    Dx = Distance*math.cos(Angle);              #Dx is the variable for the disance in the X direction.
   # log.NodeRed2(axes);                              # send the data to txt files for NodeRed to access.
    log.uniqueFile(Distance,"distance.txt");       # another way to log data for NodeRed access
    log.uniqueFile(Angle,"angle.txt"); 
    log.uniqueFile(Dy,"Dy.txt");                #Logging the Dy and Dx txt files. 
    log.uniqueFile(Dx,"Dx.txt");
    
    print ("Distance: ", Distance);             # Prints the Distance, Angle, Dx, and Dy.
    print ("Angle: ", Angle); 
    print ("Dx",Dx);
    print ("Dy",Dy);

    time.sleep(0.2);