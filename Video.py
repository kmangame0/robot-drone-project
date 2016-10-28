import time, sys
import ps_drone
from PIL import Image

##### Mainprogram begin #####

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
        #drone.groundVideo(True)  
        #drone.sdVideo()
        #drone.slowVideo()
        #drone.videoBitrate(1000)
        #drone.groundCam()
        drone.setMConfig("video:video_channel","1")
        drone.setMConfig("video:video_codec","129")
        drone.setMConfig("video:bitrate",500)
        drone.setMConfig("video:codec_fps",5)
        #drone.videoFPS(5)
        #drone.showCommands()
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
        #drone.groundVideo(True)   
        self.videoProcessing()




    def videoProcessing(self):
        time.sleep(2)
        drone = self.drone
        drone.debug = True
        print drone.getConfig()
        xtime = time.localtime()
        xSeconds = xtime[5]
        while not self.stop:
            print drone.getConfig()
        ##    y = time.localtime()
        ##    ySeconds = y[5]
        ##    if ySeconds - xSeconds > 20:
        ##        drone.land()
        ##        exit(0)
            while drone.VideoImageCount == self.IMC:
                time.sleep(0.01)
            self.IMC = drone.VideoImageCount
##            if self.processingImage == False:
##                self.processingImage = True
##                try:
##                    self.mostGreen = 1
##                    self.previousTally = 0
##                    self.currentTally = 0
##                    print "Opening Image"
##                    img = Image.open('img.png')
##
##                    if self.takeOff == False:
##                        width, height = img.size
##                        
##                        #Top Left
##                        for x in range (0,width/3):
##                            for y in range (0,height/3):
##                                r, g, b = img.getpixel((x,y))
##                                if r > 100 and r < 200 and g > 180 and g < 256 and b < 120:
##                                    self.currentTally = self.currentTally + 1
##                        if self.currentTally > self.previousTally:
##                            self.mostGreen = 1
##                        self.previousTally = self.currentTally
##                        
##                        #Top Center
##                        self.currentTally = 0
##                        for x in range (width/3,width/2):
##                            for y in range (0,height/3):
##                                r, g, b= img.getpixel((x,y))
##                                if r > 100 and r < 200 and g > 180 and g < 256 and b < 120:
##                                    self.currentTally = self.currentTally + 1
##                        if self.currentTally > self.previousTally:
##                            self.mostGreen = 2
##                        self.previousTally = self.currentTally
##
##                        #Top Right
##                        self.currentTally = 0
##                        for x in range (width/2,width):
##                            for y in range (0,height/3):
##                                r, g, b= img.getpixel((x,y))
##                                if r > 100 and r < 200 and g > 180 and g < 256 and b < 120:
##                                    self.currentTally = self.currentTally + 1
##                        if self.currentTally > self.previousTally:
##                            self.mostGreen = 3
##                        self.previousTally = self.currentTally
##                        
##                        #Left
##                        self.currentTally = 0
##                        for x in range (0,width/3):
##                            for y in range (height/3,height/2):
##                                r, g, b= img.getpixel((x,y))
##                                if r > 100 and r < 200 and g > 180 and g < 256 and b < 120:
##                                    self.currentTally = self.currentTally + 1
##                        if self.currentTally > self.previousTally:
##                            self.mostGreen = 4
##                        self.previousTally = self.currentTally
##
##                        #Center
##                        self.currentTally = 0
##                        for x in range (width/3,width/2):
##                            for y in range (height/3,height/2):
##                                r, g, b= img.getpixel((x,y))
##                                if r > 100 and r < 200 and g > 180 and g < 256 and b < 120:
##                                    self.currentTally = self.currentTally + 1
##                        if self.currentTally > self.previousTally:
##                            self.mostGreen = 5
##                        self.previousTally = self.currentTally
##
##                        #Right
##                        self.currentTally = 0
##                        for x in range (width/2,width):
##                            for y in range (height/3,height/2):
##                                r, g, b= img.getpixel((x,y))
##                                if r > 100 and r < 200 and g > 180 and g < 256 and b < 120:
##                                    self.currentTally = self.currentTally + 1
##                        if self.currentTally > self.previousTally:
##                            self.mostGreen = 6
##                        self.previousTally = self.currentTally
##
##                        #Bottom Left
##                        self.currentTally = 0
##                        for x in range (0,width/3):
##                            for y in range (height/2,height):
##                                r, g, b= img.getpixel((x,y))
##                                if r > 100 and r < 200 and g > 180 and g < 256 and b < 120:
##                                    self.currentTally = self.currentTally + 1
##                        if self.currentTally > self.previousTally:
##                            self.mostGreen = 7
##                        self.previousTally = self.currentTally
##
##                        #Bottom Center
##                        self.currentTally = 0
##                        for x in range (height/3,height/2):
##                            for y in range (height/2,height):
##                                r, g, b= img.getpixel((x,y))
##                                if r > 100 and r < 200 and g > 180 and g < 256 and b < 120:
##                                    self.currentTally = self.currentTally + 1
##                        if self.currentTally > self.previousTally:
##                            self.mostGreen = 8
##                        self.previousTally = self.currentTally
##
##                        #Bottom Right
##                        self.currentTally = 0
##                        for x in range (height/2,height):
##                            for y in range (height/2,height):
##                                r, g, b= img.getpixel((x,y))
##                                if r > 100 and r < 200 and g > 180 and g < 256 and b < 120:
##                                    self.currentTally = self.currentTally + 1
##                        if self.currentTally > self.previousTally:
##                            self.mostGreen = 9
##                        self.previousTally = self.currentTally
##                    
##            ##            if self.takeOff == True:
##            ##                self.takeOff = False
##            ##                drone.takeoff()
##            ##                time.sleep(10)
##                        print self.mostGreen
##                        self.processingImage = False
##                       
##                except:
##                    print "Error"
##                    self.processingImage = False
##                    continue


Video()
