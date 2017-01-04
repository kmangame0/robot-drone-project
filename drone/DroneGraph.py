from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np
import math
import time
import sys
import ps_drone

prevX = 0
prevY = 0
drone = ps_drone.Drone()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
counter = 0
x = time.localtime()
xSeconds = x[5]
forward = True
land = False

class Main():

    def __init__(self):                                                 
        global counter
        drone.startup()
        drone.reset()
        while (drone.getBattery()[0] == -1):  time.sleep(0.1)                       
        print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1]) 
        drone.useDemoMode(False)
        drone.takeoff()
        time.sleep(5)
        drone.setSpeed(0.1)
        time.sleep(0.1)
        drone.hover()
        
        style.use('fivethirtyeight')
        axes = plt.gca()
        axes.set_xlim([-6,6])
        axes.set_ylim([-6,6])

        rect =    patches.Rectangle(
                (-0.25, -0.25),   
                0.5,          
                0.5,          
            )
        ax1.add_patch(rect)

        ani = animation.FuncAnimation(fig, animate, interval=100)
        plt.show()

def animate(i):
    drone.hover()
    global prevX
    global prevY
    global ax1
    global x
    global xSeconds
    global forward
    global land
    y = time.localtime()
    ySeconds = y[5]
    if land == False:
        drone.getNDpackage(["demo"])
        xSpeed = (drone.NavData["demo"][4][0])/1000
        ySpeed = (drone.NavData["demo"][4][1])/1000
        yaw =  - drone.NavData["demo"][2][2]
        curX = prevX + (xSpeed*(math.cos((yaw*math.pi)/180)))
        curY = prevY + (ySpeed*(math.sin((yaw*math.pi)/180)))
        p1, = ax1.plot(curX, curY, "8")
        prevX = curX
        prevY = curY
    else:
       drone.getNDpackage(["demo"])
       xSpeed = (drone.NavData["demo"][4][0])/1000
       ySpeed = (drone.NavData["demo"][4][1])/1000
       yaw =  - drone.NavData["demo"][2][2]
       curX = prevX + (xSpeed*(math.cos((yaw*math.pi)/180)))
       curY = prevY + (ySpeed*(math.sin((yaw*math.pi)/180)))
       p1, = ax1.plot(curX, curY, "8")
       distance = math.sqrt((curX*curX)+(curY*curY))
       targetAngle = math.degrees(math.atan(curX/curY)) + 180
       prevX = curX
       prevY = curY
Main()
