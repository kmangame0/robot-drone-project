import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np
import math
import serial
import struct
import time
import socket
import select
import sys
import re
from matplotlib import style
from random import randint

port = '/dev/ttyACM0'
ser = serial.Serial(port,9600)
time.sleep(2)
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

x = 5
y = 0
angle = 30
forward = False
delPrevLine = True
updateMovement = True
axes = plt.gca()
axes.set_xlim([-200,200])
axes.set_ylim([0,200])
rect =    patches.Rectangle(
        (-30.5, 0.0),   # (x,y)
        60,          # width
        10,          # height
    )
ax1.add_patch(rect)

def updateMovementVector():
    line =    patches.Rectangle((-2.5, 10.0),5,200,0,color='green')
    ax1.add_patch(line)

def animate(i):
    global updateMovement
    if updateMovement == True:
        updateMovement = False
        updateMovementVector()
        
    global x
    global y
    global angle
    global forward
    global delPrevLine
    if delPrevLine == False:
        ax1.lines = []
        delPrevLine = True
    else:
        delPrevLine = False
        d = ord(ser.read())
        angle = ord(ser.read())
        angle = angle + 3
        x1 = 150*(math.cos(math.radians(angle)))
        y1 = 150*(math.sin(math.radians(angle)))
        ax1.plot([0,x1],[0,y1])
        x = d*(math.cos(math.radians(angle)))
        y = d*(math.sin(math.radians(angle)))
        print d
        ax1.plot(x, y, "8")
        ser.flushInput()
        ser.flushOutput()
    
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
