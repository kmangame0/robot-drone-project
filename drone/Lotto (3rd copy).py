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
playing = False
printCount = 0

startingBalance = 499.00

def green_skates(frame):
	frame = cv2.GaussianBlur(frame,(5,5),0)
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower_range = np.array([0, 100, 100], dtype=np.uint8)
	upper_range = np.array([8, 255, 255], dtype=np.uint8)
	frame = cv2.inRange(hsv, lower_range, upper_range)
	return frame

def create_rectangles(frame):
    #First Row
    # cv2.rectangle(frame, (70, 110), (120, 160), (255,0,0), 2)
    # cv2.rectangle(frame, (160, 100), (210, 150), (255,0,0), 2)
    # cv2.rectangle(frame, (260, 100), (310, 150), (255,0,0), 2)
    # cv2.rectangle(frame, (360, 100), (410, 150), (255,0,0), 2)
    # cv2.rectangle(frame, (450, 110), (500, 160), (255,0,0), 2)
    # #Second Row
    # cv2.rectangle(frame, (80, 185), (130, 235), (255,0,0), 2)
    # cv2.rectangle(frame, (170, 175), (220, 225), (255,0,0), 2)
    # cv2.rectangle(frame, (260, 175), (310, 225), (255,0,0), 2)
    # cv2.rectangle(frame, (350, 175), (400, 225), (255,0,0), 2)
    # cv2.rectangle(frame, (440, 185), (490, 235), (255,0,0), 2)
    # #Third Row
    # cv2.rectangle(frame, (85, 250), (135, 300), (255,0,0), 2)
    # cv2.rectangle(frame, (170, 250), (220, 300), (255,0,0), 2)
    # cv2.rectangle(frame, (260, 250), (310, 300), (255,0,0), 2)
    # cv2.rectangle(frame, (350, 250), (400, 300), (255,0,0), 2)
    # cv2.rectangle(frame, (430, 250), (480, 300), (255,0,0), 2)

    # cv2.rectangle(frame, (485, 350), (535, 400), (255,0,0), 2)
    # cv2.rectangle(frame, (60, 90), (500, 310), (0,255,255), 2)

    #w = 8
    #h = 13
    #cv2.rectangle(frame, (379, 387), (387, 400), (255,0,0), 1)
    for i in range(0,1):
    	#Subtract 8 each time for each number
        roi = frame[393-6:393+7, 363-4:363+4]
        # cv2.imshow('f',roi)
        # cv2.waitKey(0)
        h, w = roi.shape[:2]
        # print h
        # print w
        r = 0
        g = 0
        b = 0
        for x1 in range(0,h):
            for y1 in range(0,w):
            	# print "x1: " + str(x1)
            	# print "y1: " + str(y1)
            	# print roi[x1,y1][0]
                b = b + roi[x1,y1][0]
                g = g + roi[x1,y1][1]
                r = r + roi[x1,y1][2]
        # print "b: " + str(b)
        # print "g: " + str(g)
        # print "r: " + str(r)

    return frame

def button_pressed(frame):

    global buttonPressedOnce
    global buttonPressedTwice
    global grayButtonPressedOnce
    global playing
    global printCount
    global startingBalance

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

        if abs(r-redButtonRed) < 40000 and abs(g-redButtonGreen) < 40000 and abs(b-redButtonBlue) < 40000 or buttonPressedOnce == True:
            buttonPressedOnce = True
            if abs(r-grayButtonRed) < 40000 and abs(g-grayButtonGreen) < 40000 and abs(b-grayButtonBlue) < 40000 or grayButtonPressedOnce == True:
                grayButtonPressedOnce = True
                if abs(r-redButtonRed) < 40000 and abs(g-redButtonGreen) < 40000 and abs(b-redButtonBlue) < 40000 or buttonPressedTwice == True:
                    buttonPressedTwice = True
                    if abs(r-grayButtonRed) < 40000 and abs(g-grayButtonGreen) < 40000 and abs(b-grayButtonBlue) < 40000 or playing == True:
                        playing = True
                        if printCount == 0:
                            print "Playing"
                            startingBalance = startingBalance - 1
                            print "Balance: " + str(startingBalance)
                            printCount = printCount + 1
                        if abs(r-redButtonRed) < 40000 and abs(g-redButtonGreen) < 40000 and abs(b-redButtonBlue) < 40000:
                            playing = False
                            buttonPressedOnce = False
                            grayButtonPressedOnce = False
                            buttonPressedTwice = False
                            printCount = 0
                            print "Finished"
                            frame = get_objects(frame)

    return frame

def get_objects(frame):
    xPoints = [70,160,260,360,450,80,170,260,350,440,85,170,260,350,430]
    yPoints = [110,100,100,100,110,185,175,175,175,185,250,250,250,250,250]
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

    #Range of 2000
    zeroRed = 14335
    zeroGreen = 14076
    zeroBlue = 14420

    oneRed = 9370
    oneGreen = 9071
    oneBlue = 9463

    twoRed = 12679
    twoGreen = 12399
    twoBlue = 12779

    threeRed = 12352
    threeGreen = 12066
    threeBlue = 12440

    fourRed = 12518
    fourGreen = 12253
    fourBlue = 12605

    fiveRed = 12494
    fiveGreen = 12218
    fiveBlue = 12575

    sixRed = 133396
    sixGreen = 13124
    sixBlue = 13484

    sevenRed = 10711
    sevenGreen = 10441
    sevenBlue = 10803

    eightRed = 14798
    eightGreen = 14539
    eightBlue = 14888

    nineRed = 13786
    nineGreen = 13515
    nineBlue = 13869

    red = [zeroRed,oneRed,twoRed,threeRed,fourRed,fiveRed,sixRed,sevenRed,eightRed,nineRed]
    green = [zeroGreen,oneGreen,twoGreen,threeGreen,fourGreen,fiveGreen,sixGreen,sevenGreen,eightGreen,nineGreen]
    blue = [zeroBlue,oneBlue,twoBlue,threeBlue,fourBlue,fiveBlue,sixBlue,sevenBlue,eightBlue,nineBlue]

    
    bestRed = 999999
    bestGreen = 999999
    bestBlue = 999999
    bestIndex = 0
    for i in range(0,1):
    	#Subtract 8 each time for each number
        roi = frame[393-6:393+7, 363-4:363+4]
        # cv2.imshow('f',roi)
        # cv2.waitKey(0)
        h, w = roi.shape[:2]
        print h
        print w
        r = 0
        g = 0
        b = 0
        for x1 in range(0,h):
            for y1 in range(0,w):
            	# print "x1: " + str(x1)
            	# print "y1: " + str(y1)
                b = b + roi[x1,y1][0]
                g = g + roi[x1,y1][1]
                r = r + roi[x1,y1][2]
        # print "b: " + str(b)
        # print "g: " + str(g)
        # print "r: " + str(r)

        for i in range(0,10):
        	redDif = abs(r - red[i])
        	greenDif = abs(g-green[i])
        	blueDif = abs(b - blue[i])
        	if redDif < bestRed and greenDif < bestGreen and blueDif < bestBlue:
        		bestRed = redDif
        		bestGreen = greenDif
        		bestBlue = blueDif
        		bestIndex = i
        if bestIndex == 0:
        	print "Zero"
        elif bestIndex == 1:
        	print "One"
        elif bestIndex == 2:
        	print "Two"
        elif bestIndex == 3:
        	print "Three"
        elif bestIndex == 4:
        	print "Four"
        elif bestIndex == 5:
        	print "Five"
        elif bestIndex == 6:
        	print "Six"
        elif bestIndex == 7:
        	print "Seven"
        elif bestIndex == 8:
        	print "Eight"
        elif bestIndex == 9:
        	print "Nine"
        else:
        	print "Null"




    for i in range(0,15):
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

        if abs(r-snowFlakeRed) < 40000 and abs(g-snowFlakeGreen) < 40000 and abs(b-snowFlakeBlue) < 40000:
            temp_list.append("SnowFlake")
        elif abs(r-raceCarRed) < 40000 and abs(g-raceCarGreen) < 40000 and abs(b-raceCarBlue) < 40000:
            temp_list.append("Racecar")
        elif abs(r-hockeyGirlRed) < 40000 and abs(g-hockeyGirlGreen) < 40000 and abs(b-hockeyGirlBlue) < 40000:
            temp_list.append("Hockey Girl")
        elif abs(r-greenSkatesRed) < 40000 and abs(g-greenSkatesGreen) < 40000 and abs(b-greenSkatesBlue) < 40000:
            temp_list.append("Green Skates")
        elif abs(r-blueHockeyGuyRed) < 40000 and abs(g-blueHockeyGuyGreen) < 40000 and abs(b-blueHockeyGuyBlue) < 40000:
            temp_list.append("Blue Hockey Guy")
        elif abs(r-orangeGogglesRed) < 40000 and abs(g-orangeGogglesGreen) < 40000 and abs(b-orangleGogglesBlue) < 40000:
            temp_list.append("Orange Goggles")
        elif abs(r-purpleFourRed) < 40000 and abs(g-purpleFourGreen) < 40000 and abs(b-purpleFourBlue) < 40000:
            temp_list.append("Purple Four")
        elif abs(r-purpleGoRed) < 40000 and abs(g-purpleGoGreen) < 40000 and abs(b-purpleGoBlue) < 40000:
            temp_list.append("Purple Go")
        else:
            temp_list.append("Null")

    print temp_list[0:5]
    print temp_list[5:10]
    print temp_list[10:15]
    #verify_hsv(frame)
    return frame

def verify_hsv(frame):
    roi = frame[220-131:220+92,220-159:220+282]
    h, w = roi.shape[:2]
    frame = cv2.GaussianBlur(roi,(5,5),0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_range = np.array([12, 0, 0], dtype=np.uint8)
    upper_range = np.array([25, 255, 255], dtype=np.uint8)
    img = cv2.inRange(frame, lower_range, upper_range)
    cv2.imshow('frame',roi)
    cv2.waitKey(0)
def show_frame():
    _, frame = cap.read()
    frame = cv2.resize(frame,(0,0),fx=0.35,fy=0.35)
    frame = create_rectangles(frame)
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