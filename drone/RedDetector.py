import cv2
import numpy as np
import imutils
import SimpleCV as cv
Camera = cv.Camera(prop_set={'width':350,'height':150})
Display = cv.Display()
Threshold = 200

while True:
    Image = Camera.getImage().flipHorizontal()
    Dilate = Image.colorDistance(cv.Color.BLACK).dilate(2)
    Segment = Dilate.stretch(Threshold,255)
    Blobs = Segment.findBlobs()

    if Blobs:
        Circles = Blobs.filter([b.isCircle(0.2) for b in Blobs])
        if Circles:
            Image.drawCircle((Circles[-1].x, Circles[-1].y), Circles[-1].radius(), cv.Color.RED,3)
            if Circles [-1].x < 116:
                Center = False
                print "Left"
            if Circles[-1].x >=116 and Circles[-1].x <= 232:
                Center = True
                print "Center"
            if Circles[-1].x > 232:
                Center = False
                print "Right"
            r,g,b = Image[Circles[-1].x,Circles[-1].y]
            Threshold = (0.2126*r+0.7152*g+0.0722*b)-5
    Image.show()
