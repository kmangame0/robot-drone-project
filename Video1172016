import time, sys
import ps_drone
from PIL import Image

class Video:

    def __init__(self, *args, **kwargs):
        self.drone = ps_drone.Drone()
        drone = self.drone
        drone.startup()

        drone.reset()
        time.sleep(2)
        while (drone.getBattery()[0] == -1):      time.sleep(0.1)
        print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])
        drone.useDemoMode(False)
        drone.setConfigAllID()

        drone.setMConfig("video:video_channel","1")
        drone.setMConfig("video:video_codec","128")#Default 128
        drone.setMConfig("video:bitrate",5000) #Default 500
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
        self.previousTally = 0
        self.currentTally = 0
        self.videoProcessing()
        self.startProcessing = False


    def videoProcessing(self):
        drone = self.drone
        drone.setSpeed(0.1)
        #drone.debug = True
        #print drone.getConfig()
        xtime = time.localtime()
        xSeconds = xtime[5]
        while not self.stop:
##            print self.processingImage
##            while drone.VideoImageCount == self.IMC:
##                print "Inside Video Image Count"
##                time.sleep(0.001) #Changed from 0.01
            self.IMC = drone.VideoImageCount
            if self.processingImage == False:
                self.processingImage = True
                try:
                    self.mostGreen = 0
                    self.previousTally = 0
                    self.currentTally = 0
                    img = Image.open('img.png')
                    width, height = img.size
                    
                    if self.takeOff == False:
                        self.takeOff = True
                        time.sleep(5)
                        drone.takeoff()
                        time.sleep(15)
                        drone.hover()
                        time.sleep(2)
                        self.startProcessing = True
                        print "Taking Off"
                        

                    if self.startProcessing == True:
                        #print "Processing"
                        #Top Left
                        for x in range (0,213):
                            for y in range (0,113):
                                r, g, b = img.getpixel((x,y))
                                if r > 0 and r < 120 and g > 140 and g < 256 and b < 90:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 1
                        self.previousTally = self.currentTally
                        
                        #Top Center
                        self.currentTally = 0
                        for x in range (214,426):
                            for y in range (0,113):
                                r, g, b= img.getpixel((x,y))
                                if r > 0 and r < 120 and g > 140 and g < 256 and b < 90:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 2
                        self.previousTally = self.currentTally

                        #Top Right
                        self.currentTally = 0
                        for x in range (427,639):
                            for y in range (0,113):
                                r, g, b= img.getpixel((x,y))
                                if r > 0 and r < 120 and g > 140 and g < 256 and b < 90:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 3
                        self.previousTally = self.currentTally
                        
                        #Left
                        self.currentTally = 0
                        for x in range (0,213):
                            for y in range (113,226):
                                r, g, b= img.getpixel((x,y))
                                if r > 0 and r < 120 and g > 140 and g < 256 and b < 90:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 4
                        self.previousTally = self.currentTally

                        #Center
                        self.currentTally = 0
                        for x in range (214,426):
                            for y in range (113,226):
                                r, g, b= img.getpixel((x,y))
                                if r > 0 and r < 120 and g > 140 and g < 256 and b < 90:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 5
                        self.previousTally = self.currentTally

                        #Right
                        self.currentTally = 0
                        for x in range (427,639):
                            for y in range (113,226):
                                r, g, b= img.getpixel((x,y))
                                if r > 0 and r < 120 and g > 140 and g < 256 and b < 90:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 6
                        self.previousTally = self.currentTally

                        #Bottom Left
                        self.currentTally = 0
                        for x in range (0,213):
                            for y in range (227,339):
                                r, g, b= img.getpixel((x,y))
                                if r > 0 and r < 120 and g > 140 and g < 256 and b < 90:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 7
                        self.previousTally = self.currentTally

                        #Bottom Center
                        self.currentTally = 0
                        for x in range (214,426):
                            for y in range (227,339):
                                r, g, b= img.getpixel((x,y))
                                if r > 0 and r < 120 and g > 140 and g < 256 and b < 90:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 8
                        self.previousTally = self.currentTally

                        #Bottom Right
                        self.currentTally = 0
                        for x in range (427,639):
                            for y in range (227,339):
                                r, g, b= img.getpixel((x,y))
                                if r > 0 and r < 120 and g > 140 and g < 256 and b < 90:
                                    self.currentTally = self.currentTally + 1
                        if self.currentTally > self.previousTally:
                            self.mostGreen = 9
                        self.previousTally = self.currentTally
         
                        print "Most Green Quadrant: " + str(self.mostGreen)
                        self.processingImage = False

                        if self.mostGreen == 0:
                            drone.hover()
                            time.sleep(1)
                        elif self.mostGreen == 1:
                            drone.moveForward(0.1)
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                            drone.moveLeft(0.1)
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                        elif self.mostGreen == 2:
                            drone.moveForward(0.1)
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                        elif self.mostGreen == 3:
                            drone.moveForward(0.1)
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                            drone.moveRight(0.1)
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                        elif self.mostGreen == 4:
                            drone.moveLeft(0.1)
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                        elif self.mostGreen == 5:
                            drone.getNDpackage(["demo"])       # Info needed
                            alt = drone.NavData["demo"][3]
                            if alt > 40 and land == False:
                                if land == False:
                                    drone.moveDown(.1)
                                    time.sleep(0.1)
                                if land == False:
                                    drone.hover()
                                    time.sleep(0.1)
                            else:
                                land = True
                                drone.land()
                                exit(0)
                        elif self.mostGreen == 6:
                            drone.moveRight(0.1)
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                        elif self.mostGreen == 7:
                            drone.moveBackward(0.1)
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                            drone.moveLeft()
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                        elif self.mostGreen == 8:
                            drone.moveBackward(0.1)
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                        elif self.mostGreen == 9:
                            drone.moveBackward(0.1)
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)
                            drone.moveRight()
                            time.sleep(0.3)
                            drone.stop()
                            time.sleep(2)

                        self.mostGreen = 0
                except:
                    #print "Error"
                    self.processingImage = False
                    continue


Video()
