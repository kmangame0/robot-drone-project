import numpy as np
import cv2
import Tkinter as tk
import Image, ImageTk

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Go4Gold Analysis")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture('go4gold.mov')

buttonPressedOnce = False
buttonPressedTwice = False
grayButtonPressedOnce = False
grayButtonPressedTwice = False
playing = False

def green_skates(frame):
	frame = cv2.GaussianBlur(frame,(5,5),0)
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower_range = np.array([0, 100, 100], dtype=np.uint8)
	upper_range = np.array([8, 255, 255], dtype=np.uint8)
	frame = cv2.inRange(hsv, lower_range, upper_range)
	return frame

def create_rectangles(frame):
    #First Row
    cv2.rectangle(frame, (70, 110), (120, 160), (255,0,0), 2)
    cv2.rectangle(frame, (160, 100), (210, 150), (255,0,0), 2)
    cv2.rectangle(frame, (260, 100), (310, 150), (255,0,0), 2)
    cv2.rectangle(frame, (360, 100), (410, 150), (255,0,0), 2)
    cv2.rectangle(frame, (450, 110), (500, 160), (255,0,0), 2)
    #Second Row
    cv2.rectangle(frame, (80, 185), (130, 235), (255,0,0), 2)
    cv2.rectangle(frame, (160, 175), (210, 225), (255,0,0), 2)
    cv2.rectangle(frame, (260, 175), (310, 225), (255,0,0), 2)
    cv2.rectangle(frame, (350, 175), (400, 225), (255,0,0), 2)
    cv2.rectangle(frame, (440, 185), (490, 235), (255,0,0), 2)
    #Third Row
    cv2.rectangle(frame, (85, 250), (135, 300), (255,0,0), 2)
    cv2.rectangle(frame, (170, 250), (220, 300), (255,0,0), 2)
    cv2.rectangle(frame, (260, 250), (310, 300), (255,0,0), 2)
    cv2.rectangle(frame, (350, 250), (400, 300), (255,0,0), 2)
    cv2.rectangle(frame, (425, 250), (475, 300), (255,0,0), 2)

    cv2.rectangle(frame, (485, 350), (535, 400), (255,0,0), 2)
    return frame

def button_pressed(frame):

    global buttonPressedOnce
    global buttonPressedTwice
    global grayButtonPressedOnce
    global grayButtonPressedTwice
    global playing

    redButtonRed = 398716
    redButtonGreen = 64969
    redButtonBlue = 67688

    grayButtonRed = 175058
    grayButtonGreen = 169099
    grayButtonBlue = 176969


    for i in range(0,1):
        roi = frame[375-23:375+23, 510-23:510+23]

        h, w = roi.shape[:2]
        r = 0
        g = 0
        b = 0
        for x1 in range(0,w):
            for y1 in range(0,h):
                b = b + roi[x1,y1][0]
                g = g + roi[x1,y1][1]
                r = r + roi[x1,y1][2]
        # print "b: " + str(b)
        # print "g: " + str(g)
        # print "r: " + str(r)

        if abs(r-redButtonRed) < 20000 and abs(g-redButtonGreen) < 20000 and abs(b-redButtonBlue) < 20000 or buttonPressedOnce == True:
            buttonPressedOnce = True
            if abs(r-grayButtonRed) < 20000 and abs(g-grayButtonGreen) < 20000 and abs(b-grayButtonBlue) < 20000 or grayButtonPressedOnce == True:
                grayButtonPressedOnce = True
                if abs(r-redButtonRed) < 20000 and abs(g-redButtonGreen) < 20000 and abs(b-redButtonBlue) < 20000 or buttonPressedTwice == True:
                    buttonPressedTwice = True
                    if abs(r-grayButtonRed) < 20000 and abs(g-grayButtonGreen) < 20000 and abs(b-grayButtonBlue) < 20000 or playing == True:
                        playing = True
                        print "Playing"
                        if abs(r-redButtonRed) < 20000 and abs(g-redButtonGreen) < 20000 and abs(b-redButtonBlue) < 20000:
                            playing = False
                            buttonPressedOnce = False
                            grayButtonPressedOnce = False
                            buttonPressedTwice = False
                            print "Finished"

    return frame

def get_objects(frame):
    xPoints = [70,160,260,360,450]
    yPoints = [110,100,100,100,110]
    temp_list = []

    snowFlakeRed = 328318
    snowFlakeGreen = 398327
    snowFlakeBlue = 430573

    raceCarRed = 270598
    raceCarGreen = 275830
    raceCarBlue = 310083

    hockeyGirlRed = 291239
    hockeyGirlGreen = 338369
    hockeyGirlBlue = 326431

    greenSkatesRed = 171718
    greenSkatesGreen = 254904
    greenSkatesBlue = 211607

    blueHockeyGuyRed = 205039
    blueHockeyGuyGreen = 241072
    blueHockeyGuyBlue = 294259

    orangeGogglesRed = 311592
    orangeGogglesGreen = 282288
    orangleGogglesBlue = 235727

    purpleFourRed = 162706
    purpleFourGreen = 300532
    purpleFourBlue = 403364

    purpleGoRed = 207019
    purpleGoGreen = 292942
    purpleGoBlue = 405199

    for i in range(0,5):
        roi = frame[yPoints[i]+25-23:yPoints[i]+25+23, xPoints[i]+25-23:xPoints[i]+25+23]
        h, w = roi.shape[:2]
        r = 0
        g = 0
        b = 0
        for x1 in range(0,w):
            for y1 in range(0,h):
                b = b + roi[x1,y1][0]
                g = g + roi[x1,y1][1]
                r = r + roi[x1,y1][2]
        #if i == 1:
            # print "b: " + str(b)
            # print "g: " + str(g)
            # print "r: " + str(r)

        if abs(r-snowFlakeRed) < 20000 and abs(g-snowFlakeGreen) < 20000 and abs(b-snowFlakeBlue) < 20000:
            temp_list.append("SnowFlake")
        elif abs(r-raceCarRed) < 20000 and abs(g-raceCarGreen) < 20000 and abs(b-raceCarBlue) < 20000:
            temp_list.append("Racecar")
        elif abs(r-hockeyGirlRed) < 20000 and abs(g-hockeyGirlGreen) < 20000 and abs(b-hockeyGirlBlue) < 20000:
            temp_list.append("Hockey Girl")
        elif abs(r-greenSkatesRed) < 20000 and abs(g-greenSkatesGreen) < 20000 and abs(b-greenSkatesBlue) < 20000:
            temp_list.append("Green Skates")
        elif abs(r-blueHockeyGuyRed) < 20000 and abs(g-blueHockeyGuyGreen) < 20000 and abs(b-blueHockeyGuyBlue) < 20000:
            temp_list.append("Blue Hockey Guy")
        elif abs(r-orangeGogglesRed) < 20000 and abs(g-orangeGogglesGreen) < 20000 and abs(b-orangleGogglesBlue) < 20000:
            temp_list.append("Orange Goggles")
        elif abs(r-purpleFourRed) < 20000 and abs(g-purpleFourGreen) < 20000 and abs(b-purpleFourBlue) < 20000:
            temp_list.append("Purple Four")
        elif abs(r-purpleGoRed) < 20000 and abs(g-purpleGoGreen) < 20000 and abs(b-purpleGoBlue) < 20000:
            temp_list.append("Purple Go")
        else:
            temp_list.append("Null")

    # print temp_list
    return frame


def show_frame():
    _, frame = cap.read()
    frame = cv2.resize(frame,(0,0),fx=0.35,fy=0.35)
    frame = create_rectangles(frame)
    frame = get_objects(frame)
    frame = button_pressed(frame)
    # cv2.imshow('frame',roi)
    # cv2.waitKey(0)
    # exit(0)
    #frame = green_skates(frame)
    #cv2.line(frame, (65,175),(500,175),(255,255,255),10)
    #cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    #img = Image.fromarray(frame)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 


show_frame()  #Display 2
window.mainloop()  #Starts GUI