import serial
import struct
import time
import socket
import select
import sys

ser = serial.Serial('/dev/ttyACM0',9600)
time.sleep(2)
ser.flushInput()
ser.flushOutput()

checksum = 127 & (130 + 0 + 127)
packet = struct.pack('BBBB',130,0,127,checksum)
ser.write(packet)
checksum = 127 & (130 + 4 + 127)
packet = struct.pack('BBBB',130,4,127,checksum)
ser.write(packet)

time.sleep(10)

checksum = 127 & (130 + 0 + 127)
packet = struct.pack('BBBB',130,0,127,checksum)
ser.write(packet)
checksum = 127 & (130 + 5 + 127)
packet = struct.pack('BBBB',130,5,127,checksum)
ser.write(packet)

time.sleep(2.5)

checksum = 127 & (130 + 0 + 0)
packet = struct.pack('BBBB',130,0,0,checksum)
ser.write(packet)
checksum = 127 & (130 + 4 + 0)
packet = struct.pack('BBBB',130,4,0,checksum)
ser.write(packet)

