import time, sys
import ps_drone
from PIL import Image


class Video:

    def __init__(self, *args, **kwargs):
        self.drone = ps_drone.Drone()
        drone = self.drone
        drone.startup()

        drone.reset()
        #time.sleep(20)
        while (drone.getBattery()[0] == -1):      time.sleep(0.1)
        print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])
        drone.useDemoMode(False)
        drone.setConfigAllID()
        drone.setMConfig("video:video_channel","1")
        drone.setMConfig("video:video_codec","128")
        drone.setMConfig("video:bitrate",5000)
        drone.setMConfig("video:codec_fps",5)

        CDC = drone.ConfigDataCount
        while CDC == drone.ConfigDataCount:       time.sleep(0.0001)

        drone.startVideo()
        drone.showVideo()
        self.IMC =    drone.VideoImageCount

        self.stop =   False
        self.ground = True
        self.takeOff = False
        self.processingImage = False
        self.mostGreen = 1
        self.previousGreen = 0
        self.previousTally = 0
        self.currentTally = 0
        self.videoProcessing()
        self.startProcessing = False
        self.lostGreen = False

    def videoProcessing(self):
        self.previousGreen = 0
        drone = self.drone
        drone.setSpeed(0.1)
##        drone.getNDpackage(["demo"])  
##        firstYaw = drone.NavData["demo"][2][2]
        
        xtime = time.localtime()
        xSeconds = xtime[5]
        while not self.stop:
            self.IMC = drone.VideoImageCount
            if self.processingImage == False:
                self.processingImage = True
                try:
                    self.mostGreen = 0
                    self.previousTally = 0
                    self.currentTally = 0
                    img = Image.open('img.png')
                    
                    if self.takeOff == False:
                        self.takeOff = True
                        time.sleep(10)
                        print "Taking off"
                        drone.takeoff()
                        time.sleep(5)
                        print "Hovering"
                        drone.hover()
                        time.sleep(1)
                        self.processingImage = False
                        print "Done Calibrating"
##                        drone.getNDpackage(["demo"])  
##                        secondYaw = drone.NavData["demo"][2][2]
##                        firstYaw = firstYaw + secondYaw
                        self.processingImage = False

                    else:

##                        if abs(secondYaw-firstYaw) > 3.5:
##                            drone.getNDpackage(["demo"])  
##                            secondYaw = drone.NavData["demo"][2][2]
##                            if secondYaw > firstYaw:
##                                drone.turnAngle(-2,0.25)
##                            else:
##                                drone.turnAngle(2,0.25)
##                            self.processingImage = False

                        #Top Left
                        for x in range (0,53):
                            for y in range (0,30):
                                r, g, b = img.getpixel((x,y))
                                if r > 30 and r < 141 and g < 15 and b < 41:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 1
                        self.previousTally = self.currentTally

                        #Top Center
                        self.currentTally = 0
                        for x in range (54,106):
                            for y in range (0,30):
                                r, g, b= img.getpixel((x,y))
                                if r > 30 and r < 141 and g < 15 and b < 41:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 2
                        self.previousTally = self.currentTally
                        
                        #Top Right
                        self.currentTally = 0
                        for x in range (107,159):
                            for y in range (0,30):
                                r, g, b= img.getpixel((x,y))
                                if r > 30 and r < 141 and g < 15 and b < 41:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 3
                        self.previousTally = self.currentTally

                        #Left
                        self.currentTally = 0
                        for x in range (0,53):
                            for y in range (30,60):
                                r, g, b= img.getpixel((x,y))
                                if r > 30 and r < 141 and g < 15 and b < 41:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 4
                        self.previousTally = self.currentTally

                        #Center
                        self.currentTally = 0
                        for x in range (54,106):
                            for y in range (30,60):
                                r, g, b= img.getpixel((x,y))
                                if r > 30 and r < 141 and g < 15 and b < 41:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 5
                        self.previousTally = self.currentTally

                        #Right
                        self.currentTally = 0
                        for x in range (107,159):
                            for y in range (30,60):
                                r, g, b= img.getpixel((x,y))
                                if r > 30 and r < 141 and g < 15 and b < 41:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 6
                        self.previousTally = self.currentTally

                        #Bottom Left
                        self.currentTally = 0
                        for x in range (0,53):
                            for y in range (60,90):
                                r, g, b= img.getpixel((x,y))
                                if r > 30 and r < 141 and g < 15 and b < 41:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 7
                        self.previousTally = self.currentTally

                        #Bottom Center
                        self.currentTally = 0
                        for x in range (54,106):
                            for y in range (60,90):
                                r, g, b= img.getpixel((x,y))
                                if r > 30 and r < 141 and g < 15 and b < 41:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 8
                        self.previousTally = self.currentTally

                        #Bottom Right
                        self.currentTally = 0
                        for x in range (107,159):
                            for y in range (60,90):
                                r, g, b= img.getpixel((x,y))
                                if r > 30 and r < 141 and g < 15 and b < 41:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 9
                        self.previousTally = self.currentTally
             
                        print "Most Red Quadrant: " + str(self.mostGreen)

                        if self.mostGreen == 0:
                            print "Lost Green"
                            self.mostGreen = self.previousGreen
                            if self.previousGreen == 1:
                                self.mostGreen = 9
                            elif self.previousGreen == 2:
                                self.mostGreen = 8
                            elif self.previousGreen == 3:
                                self.mostGreen = 7
                            elif self.previousGreen == 4:
                                self.mostGreen = 6
                            elif self.previousGreen == 5:
                                self.mostGreen = 5
                            elif self.previousGreen == 6:
                                self.mostGreen = 4
                            elif self.previousGreen == 7:
                                self.mostGreen = 3
                            elif self.previousGreen == 8:
                                self.mostGreen = 2
                            elif self.previousGreen == 9:
                                self.mostGreen = 1
                        if self.mostGreen == 1:
                            print "Forward, Left"
                            drone.moveForward(0.1)
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                            drone.moveLeft(0.1)
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                        if self.mostGreen == 2:
                            print "Forward"
                            drone.moveForward(0.1)
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                        if self.mostGreen == 3:
                            print "Forward, Right"
                            drone.moveForward(0.1)
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                            drone.moveRight(0.1)
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                        if self.mostGreen == 4:
                            print "Left"
                            drone.moveLeft(0.1)
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                        if self.mostGreen == 5:
                            #if alt < 90:
                            drone.land()
                            #time.sleep(1)
                            self.processingImage = True
                            self.stop = True
                            
                        if self.mostGreen == 6:
                            print "Right"
                            drone.moveRight(0.1)
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                        if self.mostGreen == 7:
                            print "Back, Left"
                            drone.moveBackward(0.1)
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                            drone.moveLeft()
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                        if self.mostGreen == 8:
                            print "Back"
                            drone.moveBackward(0.1)
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                        if self.mostGreen == 9:
                            print "Back, Right"
                            drone.moveBackward(0.1)
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)
                            drone.moveRight()
                            time.sleep(0.1)
                            drone.stop()
                            #time.sleep(1)

                        self.processingImage = False
                        if self.mostGreen != 0:
                            self.previousGreen = self.mostGreen
                except:
                    #print "Error"
                    self.processingImage = False
                    continue


Video()
