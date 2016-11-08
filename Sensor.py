import serial
import struct
import time
import socket
import select
import sys
from visual import *

ser = serial.Serial('/dev/ttyACM0',9600)
measuringRod = cylinder( radius= .1, length=6, color=color.yellow, pos=(-3,-2,0))
lengthLabel = label(pos=(0,5,0), text='Distance', box=false, height=30)
target=box(pos=(0,-.5,0), length=.2, width=1, height=3, color=color.red)
while (1==1):  
    rate(20)
    if (ser.inWaiting()>0):
        data = ser.readline()
        print data
        try:
            distance = float(data)
            measuringRod.length=distance 
            target.pos=(-3+distance,-.5,0)
            myLabel= 'Distance: ' + data 
            lengthLabel.text = myLabel
        except:
            continue
