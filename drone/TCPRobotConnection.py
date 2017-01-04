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
speed = 0
x1 = 0
x2 = 0
prevX1 = 0
motor1Speed = 0
motor2Speed = 0
prevX2 = 0
called = False

##Begin socket handling
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "141.209.191.46"
port = 12345
size = 1024
s.bind((host,port))
s.listen(5)

def run():
    called = True
    input = [c,sys.stdin]
    ser.flushInput()
    ser.flushOutput()
    prevX1 = 0
    prevX2 = 0
    speed = 0
    motor1Speed = 0
    motor2Speed = 0
    x1 = 0
    x2 = 0
    while running:
        ser.flushInput()
        ser.flushOutput()
        r,_,_ = select.select(input,[],[])
        if r:
            data = c.recv(size)
            if data[0] == "y":
                x2 = data.split("y",1)[1]
                ##Make sure to compensate for a negative. Split appropriately
                ##Splits -X.XX
                if data[1] == "-":
                    x2 = data[1:5]
                    x2 = x2.strip()
                    print "x2: " + x2
                else:
                    ##Splits X.XX
                    x2 = data[1:4]
                    x2 = x2.strip()
                    print "x2: " + x2
            if data[0] == "a":
                x1 = data.split("a",1)[1]
                ##Make sure to compensate for a negative. Split appropriately
                ##Splits -X.XX
                if data[1] == "-":
                    x1 = data[1:5]
                    x1 = x1.strip()
                    print "x1: " + x1
                else:
                    ##Splits X.XX
                    x1 = data[1:4]
                    x1 = x1.strip()
                    print "x1: " + x1
            ##Checking for forward speed
            if float(x2) < -0.2 and float(x1) > -0.1 and float(x1) < 0.1:
                print("wow")
                if float(x2) <= float(prevX2):
                    if motor1Speed < 125:
                        motor1Speed += 10
                    if motor1Speed > 125:
                        motor1Speed = 125
                    motor2Speed = motor1Speed
                    checksum = 127 & (130 + 0 + motor1Speed)
                    packet = struct.pack('BBBB',130,0,motor1Speed,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 4 + motor2Speed)
                    packet = struct.pack('BBBB',130,4,motor2Speed,checksum)
                    ser.write(packet)
                else:
                    if motor1Speed > -1:
                        motor1Speed -= 10
                    if motor1Speed < 0:
                        motor1Speed = 0
                    motor2Speed = motor1Speed
                    checksum = 127 & (130 + 0 + motor1Speed)
                    packet = struct.pack('BBBB',130,0,motor1Speed,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 4 + motor2Speed)
                    packet = struct.pack('BBBB',130,4,motor2Speed,checksum)
                    ser.write(packet)
            ##Checking for upper left speed
            elif float(x2) < -0.2 and float(x1) >= -1.0 and float(x1) < 0.1:
                print("true22")
                if float(x2) <= float(prevX2):
                    if motor1Speed >= 0:
                        motor1Speed -= 3
                    if motor1Speed < 0:
                        motor1Speed = 0
                    if motor2Speed >= 0:
                        motor2Speed -= 1
                    if motor2Speed < 0:
                        motor2Speed = 0
                    checksum = 127 & (130 + 0 + motor1Speed)
                    packet = struct.pack('BBBB',130,0,motor1Speed,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 4 + motor2Speed)
                    packet = struct.pack('BBBB',130,4,motor2Speed,checksum)
                    ser.write(packet)
            ##Checking for upper right speed
            elif float(x2) < -0.2 and float(x1) >= 0.1:
                print("true5")
                if float(x2) <= float(prevX2):
                    if motor1Speed >= 0:
                        motor1Speed -= 1
                    if motor1Speed < 0:
                        motor1Speed = 0
                    if motor2Speed >= 0:
                        motor2Speed -= 3
                    if motor2Speed < 0:
                        motor2Speed = 0
                    checksum = 127 & (130 + 0 + motor1Speed)
                    packet = struct.pack('BBBB',130,0,motor1Speed,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 4 + motor2Speed)
                    packet = struct.pack('BBBB',130,4,motor2Speed,checksum)
                    ser.write(packet)
            ##Checking for backward speed
            elif float(x2) > 0.2 and float(x1) > -0.1 and float(x1) < 0.1:
                print("here3")
                if float(x2) >= float(prevX2):
                    if speed < 125:
                        speed += 10
                    if speed > 125:
                        speed = 125
                    checksum = 127 & (130 + 1 + speed)
                    packet = struct.pack('BBBB',130,1,speed,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 5 + speed)
                    packet = struct.pack('BBBB',130,5,speed,checksum)
                    ser.write(packet)
                else:
                    if speed > -1:
                        speed -= 10
                    if speed < 0:
                        speed = 0
                    checksum = 127 & (130 + 1 + speed)
                    packet = struct.pack('BBBB',130,1,speed,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 5 + speed)
                    packet = struct.pack('BBBB',130,5,speed,checksum)
                    ser.write(packet)
            ##Checking for left speed        
            elif float(x1) < -0.2 and float(x2) >= -0.1 and float(x2) <= 0.1:
                print("true2")
                if float(x1) <= float(prevX1):
                    if motor2Speed < 125:
                        motor2Speed += 10
                    if motor2Speed > 125:
                        motor2Speed = 125
                    checksum = 127 & (130 + 1 + 0)
                    packet = struct.pack('BBBB',130,1,0,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 4 + motor2Speed)
                    packet = struct.pack('BBBB',130,4,motor2Speed,checksum)
                    ser.write(packet)
                else:
                    if speed > -1:
                        speed -= 10
                    if speed < 0:
                        speed = 0
                    checksum = 127 & (130 + 1 + 0)
                    packet = struct.pack('BBBB',130,1,0,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 4 + motor2Speed)
                    packet = struct.pack('BBBB',130,4,motor2Speed,checksum)
                    ser.write(packet)
            ##checking for right speed
            elif float(x1) > 0.9 and float(x2) >= -0.1 and float(x2) <= 0.1:
                print("here")
                if float(x1) >= float(prevX1):
                    print("here")
                    if motor1Speed < 125:
                        motor1Speed += 10
                    if motor1Speed > 125:
                        motor1Speed = 125
                    checksum = 127 & (130 + 0 + motor1Speed)
                    packet = struct.pack('BBBB',130,0,motor1Speed,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 5 + 0)
                    packet = struct.pack('BBBB',130,5,0,checksum)
                    ser.write(packet)
                else:
                    print("kellen")
                    if speed > -1:
                        speed -= 10
                    if speed < 0:
                        speed = 0
                    checksum = 127 & (130 + 0 + speed)
                    packet = struct.pack('BBBB',130,0,speed,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 5 + speed)
                    packet = struct.pack('BBBB',130,5,speed,checksum)
                    ser.write(packet)
            ##Checking for lower right speed
            elif float(x2) <= 1.0 and float(x2) > 0.1 and float(x1) > 0.1:
                print("true1w")
                if float(x1) <= float(prevX1):
                    if motor1Speed >= 0:
                        motor1Speed -= 1
                    if motor1Speed < 0:
                        motor1Speed = 0
                    if motor2Speed >= 0:
                        motor2Speed -= 3
                    if motor2Speed < 0:
                        motor2Speed = 0
                    checksum = 127 & (130 + 1 + motor1Speed)
                    packet = struct.pack('BBBB',130,1,motor1Speed,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 5 + motor2Speed)
                    packet = struct.pack('BBBB',130,5,motor2Speed,checksum)
                    ser.write(packet)
             ##Checking for lower left speed
            elif float(x2) <= 1.0 and float(x2) > 0.1 and float(x1) < 0.0:
                print("true1wwwwww")
                if float(x1) <= float(prevX1):
                    if motor1Speed >= 0:
                        motor1Speed -= 3
                    if motor1Speed < 0:
                        motor1Speed = 0
                    if motor2Speed >= 0:
                        motor2Speed -= 1
                    if motor2Speed < 0:
                        motor2Speed = 0
                    checksum = 127 & (130 + 1 + motor1Speed)
                    packet = struct.pack('BBBB',130,1,motor1Speed,checksum)
                    ser.write(packet)
                    checksum = 127 & (130 + 5 + motor2Speed)
                    packet = struct.pack('BBBB',130,5,motor2Speed,checksum)
                    ser.write(packet)
####            elif float(x2) < -0.2 and float(x1) < 0.2:
####                motor1Speed = speed
####                motor2Speed = speed
####                if motor1Speed > -1:
####                    motor1Speed -= 10
####                checksum = 127 & (130 + 0 + motor1Speed)
####                packet = struct.pack('BBBB',130,0,motor1Speed,checksum)
####                ser.write(packet)
####                checksum = 127 & (130 + 4 + motor2Speed)
####                packet = struct.pack('BBBB',130,4,motor2Speed,checksum)
####                ser.write(packet)
####            elif float(x2) > 0.2 and float(x1) > 0.2:
####                motor1Speed = speed
####                motor2Speed = speed
####                if motor2Speed > -1:
####                    motor2Speed -= 10
####                checksum = 127 & (130 + 0 + motor1Speed)
####                packet = struct.pack('BBBB',130,0,motor1Speed,checksum)
####                ser.write(packet)
####                checksum = 127 & (130 + 4 + motor2Speed)
####                packet = struct.pack('BBBB',130,4,motor2Speed,checksum)
####                ser.write(packet)
####            elif float(x1) < -0.2 and float(x2) > 0.2:
####                motor1Speed = speed
####                motor2Speed = speed
####                if motor2Speed > -1:
####                    motor2Speed -= 10
####                checksum = 127 & (130 + 0 + motor1Speed)
####                packet = struct.pack('BBBB',130,0,motor1Speed,checksum)
####                ser.write(packet)
####                checksum = 127 & (130 + 4 + motor2Speed)
####                packet = struct.pack('BBBB',130,4,motor2Speed,checksum)
####                ser.write(packet)
            else:
                print("inside else")
                speed = 0
                checksum = 127 & (130 + 0 + speed)
                packet = struct.pack('BBBB',130,0,speed,checksum)
                ser.write(packet)
                checksum = 127 & (130 + 4 + speed)
                packet = struct.pack('BBBB',130,4,speed,checksum)
                ser.write(packet)
            
        prevX1 = float(x1)
        prevX2 = float(x2)
       
        ser.flushInput()
        ser.flushOutput()
           
            
while called == False:
    c, addr = s.accept()
    print("Connection accepted from " + repr(addr[1]))
    c.send("Thank you for connecting")
    running = 1
    checksum = 127 & (130 + 0 + 0)
    packet = struct.pack('BBBB',130,0,0,checksum)
    ser.write(packet)
    checksum = 127 & (130 + 4 + 0)
    packet = struct.pack('BBBB',130,4,0,checksum)
    ser.write(packet)
    run()

