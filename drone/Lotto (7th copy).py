import numpy as np
import cv2
import Tkinter as tk
import Image, ImageTk
from decimal import Decimal
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
                            #print "Playing"
                            startingBalance = startingBalance - 1
                            print "Starting Balance: " + str(startingBalance)
                            printCount = printCount + 1
                        if abs(r-redButtonRed) < 40000 and abs(g-redButtonGreen) < 40000 and abs(b-redButtonBlue) < 40000:
                            playing = False
                            buttonPressedOnce = False
                            grayButtonPressedOnce = False
                            buttonPressedTwice = False
                            printCount = 0
                            #print "Finished"
                            frame = get_objects(frame)

    return frame

def get_objects(frame):
    global startingBalance

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

    blueHockeyGuyRed2 = 199047
    blueHockeyGuyGreen2 = 233764
    blueHockeyGuyBlue2 = 288266

    blueHockeyGuyRed3 = 222185
    blueHockeyGuyGreen3 = 329012
    blueHockeyGuyBlue3 = 369990

    orangeGogglesRed = 311592
    orangeGogglesGreen = 282288
    orangleGogglesBlue = 235727

    purpleFourRed = 162706
    purpleFourGreen = 300532
    purpleFourBlue = 403364

    purpleGoRed = 207019
    purpleGoGreen = 292942
    purpleGoBlue = 405199

    raceCarRed2 = 257122
    raceCarGreen2 = 339750
    raceCarBlue2 = 366230

    greenSkatesRed2 = 199178
    greenSkatesGreen2 = 330829
    greenSkatesBlue2 = 309833

    orangeGogglesRed2 = 283968
    orangeGogglesGreen2 = 315100
    orangleGogglesBlue2 = 291098

    hockeyGirlRed2 = 270536
    hockeyGirlGreen2 = 384291
    hockeyGirlBlue2 = 390927

    hockeyGirlRed3 = 300739
    hockeyGirlGreen3 = 325316
    hockeyGirlBlue3 = 305741

    goForGoldRed = 350841
    goForGoldGreen = 305410
    goForGoldBlue = 276953

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

    noNumberRed = 3000
    noNumberGreen = 3000
    noNumberBlue = 3000
    # nineRed = 14279
    # nineGreen = 14005
    # nineBlue = 14368

    red = [zeroRed,oneRed,twoRed,threeRed,fourRed,fiveRed,sixRed,sevenRed,eightRed,nineRed]
    green = [zeroGreen,oneGreen,twoGreen,threeGreen,fourGreen,fiveGreen,sixGreen,sevenGreen,eightGreen,nineGreen]
    blue = [zeroBlue,oneBlue,twoBlue,threeBlue,fourBlue,fiveBlue,sixBlue,sevenBlue,eightBlue,nineBlue]

    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    num9 = 0
    num10 = 0
    numbers = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]

    xPositionForNumbers = [346,354,362,375,383,405,425,438,446] #405
    finalNumbers = [0,0,0,0,0,0,0,0,0]
    bestRed = 999999
    bestGreen = 999999
    bestBlue = 999999
    bestIndex = -1
    BigWin = False
    for cnt in range(0,9):
        #Subtract 8 each time for each number
        roi = frame[393-6:393+7, xPositionForNumbers[cnt]-4:xPositionForNumbers[cnt]+4]
        # if cnt == 5:
        #   cv2.imshow('f',roi)
        #   cv2.waitKey(0)
        h, w = roi.shape[:2]
        # print h
        # print w
        r = 0
        g = 0
        b = 0
        bestRed = 999999
        bestGreen = 999999
        bestBlue = 999999
        bestIndex = -1
        redDif = 0
        greenDif = 0
        blueDif = 0
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
            roi = frame[391-4:391+4, xPositionForNumbers[cnt]-4:xPositionForNumbers[cnt]+4]
            h, w = roi.shape[:2]
            # print h
            # print w
            r = 0
            g = 0
            b = 0
            bestRed = 999999
            bestGreen = 999999
            bestBlue = 999999
            bestIndex = -1
            redDif = 0
            greenDif = 0
            blueDif = 0
            for x1 in range(0,h):
                for y1 in range(0,w):
                    # print "x1: " + str(x1)
                    # print "y1: " + str(y1)
                    b = b + roi[x1,y1][0]
                    g = g + roi[x1,y1][1]
                    r = r + roi[x1,y1][2]
            #print "b: " + str(b)
            # print "g: " + str(g)
            #print "r: " + str(r)
            #for nine:
            #r:8493
            #g:8323
            #b:8551
            # cv2.imshow('f',roi)
            # cv2.waitKey(0)
            if abs(r-8493) < 300 and abs(g - 8323) < 300 and abs(b-8551) < 300:
                bestIndex = 9
                #print "Nine"
            elif abs(r-8493) > 300 and abs(r-8493) < 1000 and abs(g - 8323) > 300 and abs(g - 8323) < 1000 and abs(b-8551) > 300 and abs(b-8551) < 1000:
                bestIndex = 0
                #print "Zero"
            else:
                bestIndex = 6
                #print "Six"

        elif bestIndex == 1:

            #We choose 1 because 1 is the one with the lowest rgb values
            #print "One"
            # print r
            if r < 4000:
                bestIndex = 0
            else:
                if cnt > 4:
                    print "Big Win!"
                    cnt = cnt
                    xPositionForNumbers = [346,354,362,375,383,421,429,442,450]
                    roi = frame[393-6:393+7, xPositionForNumbers[cnt]-4:xPositionForNumbers[cnt]+4]
                    # cv2.imshow('f',roi)
                    # cv2.waitKey(0)
                else:
                    bestIndex = 1


        elif bestIndex == 2:
            roi = frame[391-4:391+4, xPositionForNumbers[cnt]-4:xPositionForNumbers[cnt]+4]
            h, w = roi.shape[:2]
            # print h
            # print w
            r = 0
            g = 0
            b = 0
            bestRed = 999999
            bestGreen = 999999
            bestBlue = 999999
            bestIndex = -1
            redDif = 0
            greenDif = 0
            blueDif = 0
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
            #for nine:
            #r:8493
            #g:8323
            #b:8551
            # cv2.imshow('f',roi)
            # cv2.waitKey(0)
            if abs(r-6767) < 300 and abs(g - 6589) < 300 and abs(b-6817) < 300:
                bestIndex = 4
                #print "Four"
            else:
                bestIndex = 2
                #print "Two"
        elif bestIndex == 3:
            #bestIndex = 3
            #print "Three"
            roi = frame[391-4:391+4, xPositionForNumbers[cnt]-4:xPositionForNumbers[cnt]+4]
            h, w = roi.shape[:2]
            # print h
            # print w
            r = 0
            g = 0
            b = 0
            bestRed = 999999
            bestGreen = 999999
            bestBlue = 999999
            bestIndex = -1
            redDif = 0
            greenDif = 0
            blueDif = 0
            for x1 in range(0,h):
                for y1 in range(0,w):
                    # print "x1: " + str(x1)
                    # print "y1: " + str(y1)
                    b = b + roi[x1,y1][0]
                    g = g + roi[x1,y1][1]
                    r = r + roi[x1,y1][2]
            print "b: " + str(b)
            print "g: " + str(g)
            print "r: " + str(r)
            #for nine:
            #r:8493
            #g:8323
            #b:8551
            # cv2.imshow('f',roi)
            # cv2.waitKey(0)
            if abs(r-6818) < 300 and abs(g - 6640) < 300 and abs(b-6874) < 300:
                bestIndex = 3
                #print "Four"
            else:
                bestIndex = 5
                #print "Two"
        elif bestIndex == 4:
            roi = frame[391-4:391+4, xPositionForNumbers[cnt]-4:xPositionForNumbers[cnt]+4]
            h, w = roi.shape[:2]
            # print h
            # print w
            r = 0
            g = 0
            b = 0
            bestRed = 999999
            bestGreen = 999999
            bestBlue = 999999
            bestIndex = -1
            redDif = 0
            greenDif = 0
            blueDif = 0
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
            #for nine:
            #r:8493
            #g:8323
            #b:8551
            # cv2.imshow('f',roi)
            # cv2.waitKey(0)
            if abs(r-6767) < 300 and abs(g - 6589) < 300 and abs(b-6817) < 300:
                bestIndex = 4
                #print "Four"
            else:
                bestIndex = 2
                #print "Two"
        elif bestIndex == 5:
            #bestIndex = 5
            #print "Five"
             #bestIndex = 3
            #print "Three"
            roi = frame[391-4:391+4, xPositionForNumbers[cnt]-4:xPositionForNumbers[cnt]+4]
            h, w = roi.shape[:2]
            # print h
            # print w
            r = 0
            g = 0
            b = 0
            bestRed = 999999
            bestGreen = 999999
            bestBlue = 999999
            bestIndex = -1
            redDif = 0
            greenDif = 0
            blueDif = 0
            for x1 in range(0,h):
                for y1 in range(0,w):
                    # print "x1: " + str(x1)
                    # print "y1: " + str(y1)
                    b = b + roi[x1,y1][0]
                    g = g + roi[x1,y1][1]
                    r = r + roi[x1,y1][2]
            print "b: " + str(b)
            print "g: " + str(g)
            print "r: " + str(r)
            #for nine:
            #r:8493
            #g:8323
            #b:8551
            # cv2.imshow('f',roi)
            # cv2.waitKey(0)
            if abs(r-6818) < 300 and abs(g - 6640) < 300 and abs(b-6874) < 300:
                bestIndex = 3
                #print "Four"
            else:
                bestIndex = 5
                #print "Two"
        elif bestIndex == 6:
            bestIndex = 6
            #print "Six"
        elif bestIndex == 7:
            bestIndex = 7
            roi = frame[391-4:391+4, xPositionForNumbers[cnt]-4:xPositionForNumbers[cnt]+4]
            h, w = roi.shape[:2]
            # print h
            # print w
            r = 0
            g = 0
            b = 0
            bestRed = 999999
            bestGreen = 999999
            bestBlue = 999999
            bestIndex = -1
            redDif = 0
            greenDif = 0
            blueDif = 0
            for x1 in range(0,h):
                for y1 in range(0,w):
                    # print "x1: " + str(x1)
                    # print "y1: " + str(y1)
                    b = b + roi[x1,y1][0]
                    g = g + roi[x1,y1][1]
                    r = r + roi[x1,y1][2]
            print "b: " + str(b)
            print "g: " + str(g)
            print "r: " + str(r)
            #for nine:
            #r:8493
            #g:8323
            #b:8551
            # cv2.imshow('f',roi)
            # cv2.waitKey(0)
            #print "Seven"
            if abs(r-6790) < 300 and abs(g - 6625) < 300 and abs(b-6857) < 300:
                bestIndex = 7
                #print "Four"
            else:
                bestIndex = 1
                #print "Two"
        elif bestIndex == 8:
            bestIndex = 8
            #print "Eight"
        elif bestIndex == 9:
            roi = frame[391-4:391+4, xPositionForNumbers[cnt]-4:xPositionForNumbers[cnt]+4]
            h, w = roi.shape[:2]
            # print h
            # print w
            r = 0
            g = 0
            b = 0
            bestRed = 999999
            bestGreen = 999999
            bestBlue = 999999
            bestIndex = -1
            redDif = 0
            greenDif = 0
            blueDif = 0
            for x1 in range(0,h):
                for y1 in range(0,w):
                    # print "x1: " + str(x1)
                    # print "y1: " + str(y1)
                    b = b + roi[x1,y1][0]
                    g = g + roi[x1,y1][1]
                    r = r + roi[x1,y1][2]
            # print "b: " + str(b)
            #  print "g: " + str(g)
            #print "r: " + str(r)
            #for nine:
            #r:8493
            #g:8323
            #b:8551
            if abs(r-8493) < 300 and abs(g - 8323) < 300 and abs(b-8551) < 300:
                bestIndex = 9
                #print "Nine"
            elif abs(r-8493) > 300 and abs(r-8493) < 1000 and abs(g - 8323) > 300 and abs(g - 8323) < 1000 and abs(b-8551) > 300 and abs(b-8551) < 1000:
                bestIndex = 0
                #print "Zero"
            else:
                bestIndex = 6
                #print "Six"
            # cv2.imshow('f',roi)
            # cv2.waitKey(0)
        else:
            print "Null"
        # print bestIndex
        finalNumbers[cnt] = bestIndex
    print finalNumbers

    bal = str(finalNumbers[0]) + str(finalNumbers[1])+str(finalNumbers[2]) + "." + str(finalNumbers[3])+str(finalNumbers[4])
    bal = float(bal)
    winnings = float(str(finalNumbers[5]) + str(finalNumbers[6]) + "." + str(finalNumbers[7]) + str(finalNumbers[8]))
    #print winnings

    startingBalance = startingBalance + winnings
    # print bal
    print "New Balance: " + str(startingBalance)




    red2 = [snowFlakeRed,raceCarRed,hockeyGirlRed,greenSkatesRed,orangeGogglesRed,purpleFourRed, purpleGoRed,blueHockeyGuyRed2,blueHockeyGuyRed,raceCarRed2,blueHockeyGuyRed3,greenSkatesRed2,orangeGogglesRed2,hockeyGirlRed2, hockeyGirlRed3,goForGoldRed]
    green2 = [snowFlakeGreen,raceCarGreen,hockeyGirlGreen,greenSkatesGreen,orangeGogglesGreen,purpleFourGreen,purpleGoGreen,blueHockeyGuyGreen2,blueHockeyGuyGreen,raceCarGreen2,blueHockeyGuyGreen3,greenSkatesGreen2,orangeGogglesGreen2,hockeyGirlGreen2,hockeyGirlGreen3,goForGoldGreen]
    blue2 = [snowFlakeBlue,raceCarBlue,hockeyGirlBlue,greenSkatesBlue,orangleGogglesBlue,purpleFourBlue,purpleGoBlue,blueHockeyGuyBlue2,blueHockeyGuyBlue,raceCarBlue2,blueHockeyGuyBlue3,greenSkatesBlue2,orangleGogglesBlue2,hockeyGirlBlue2,hockeyGirlBlue3,goForGoldBlue]

    for cnt in range (0,15):
        bestRed = 999999
        bestGreen = 999999
        bestBlue = 999999
        bestIndex = -1
        redDif = 0
        greenDif = 0
        blueDif = 0
        error = 0
        prevError = 999999
        roi = frame[yPoints[cnt]+25-23:yPoints[cnt]+25+23, xPoints[cnt]+25-23:xPoints[cnt]+25+23]
        h, w = roi.shape[:2]
        r = 0
        g = 0
        b = 0
        for x1 in range(0,w):
            for y1 in range(0,h):
                b = b + roi[x1,y1][0]
                g = g + roi[x1,y1][1]
                r = r + roi[x1,y1][2]
        if cnt == 3:
            print "b: " + str(b)
            print "g: " + str(g)
            print "r: " + str(r)
        for i in range(0,16):
            redDif = abs(r - red2[i])
            greenDif = abs(g-green2[i])
            blueDif = abs(b - blue2[i])
            error = redDif + greenDif + blueDif
            #We want to compute the error for each image and select the one with the lowest error:
            if error < prevError:
                bestRed = redDif
                bestGreen = greenDif
                bestBlue = blueDif
                bestIndex = i
                #print bestIndex
                prevError = error
        if bestIndex == 0:
            temp_list.append("SnowFlake")
        elif bestIndex == 1:
            temp_list.append("Racecar")
        elif bestIndex == 2:
            temp_list.append("Hockey Girl")
        elif bestIndex == 3:
            temp_list.append("Green Skates")
        elif bestIndex == 4:
            temp_list.append("Orange Goggles")
        elif bestIndex == 5:
            temp_list.append("Purple Four")
        elif bestIndex == 6:
            temp_list.append("Purple Go")
        elif bestIndex == 7:
            temp_list.append("Hockey Guy")
        elif bestIndex == 8:
            temp_list.append("Hockey Guy")
        elif bestIndex == 9:
            temp_list.append("Racecar")
        elif bestIndex == 10:
            temp_list.append("Hockey Guy")
        elif bestIndex == 11:
            temp_list.append("Green Skates")
        elif bestIndex == 12:
            temp_list.append("Orange Goggles")
        elif bestIndex == 13:
            temp_list.append("Hockey Girl")
        elif bestIndex == 14:
            temp_list.append("Hockey Girl") 
        elif bestIndex == 15:
            temp_list.append("Gold!")   
        else:
            temp_list.append("Null")






    # for i in range(0,15):
    #     roi = frame[yPoints[i]+25-23:yPoints[i]+25+23, xPoints[i]+25-23:xPoints[i]+25+23]
    #     h, w = roi.shape[:2]
    #     r = 0
    #     g = 0
    #     b = 0
    #     for x1 in range(0,w):
    #         for y1 in range(0,h):
    #             b = b + roi[x1,y1][0]
    #             g = g + roi[x1,y1][1]
    #             r = r + roi[x1,y1][2]

    #     if abs(r-snowFlakeRed) < 40000 and abs(g-snowFlakeGreen) < 40000 and abs(b-snowFlakeBlue) < 40000:
    #         temp_list.append("SnowFlake")
    #     elif abs(r-raceCarRed) < 40000 and abs(g-raceCarGreen) < 40000 and abs(b-raceCarBlue) < 40000:
    #         temp_list.append("Racecar")
    #     elif abs(r-hockeyGirlRed) < 40000 and abs(g-hockeyGirlGreen) < 40000 and abs(b-hockeyGirlBlue) < 40000:
    #         temp_list.append("Hockey Girl")
    #     elif abs(r-greenSkatesRed) < 40000 and abs(g-greenSkatesGreen) < 40000 and abs(b-greenSkatesBlue) < 40000:
    #         temp_list.append("Green Skates")
    #     elif abs(r-blueHockeyGuyRed) < 40000 and abs(g-blueHockeyGuyGreen) < 40000 and abs(b-blueHockeyGuyBlue) < 40000:
    #         temp_list.append("Blue Hockey Guy")
    #     elif abs(r-orangeGogglesRed) < 40000 and abs(g-orangeGogglesGreen) < 40000 and abs(b-orangleGogglesBlue) < 40000:
    #         temp_list.append("Orange Goggles")
    #     elif abs(r-purpleFourRed) < 40000 and abs(g-purpleFourGreen) < 40000 and abs(b-purpleFourBlue) < 40000:
    #         temp_list.append("Purple Four")
    #     elif abs(r-purpleGoRed) < 40000 and abs(g-purpleGoGreen) < 40000 and abs(b-purpleGoBlue) < 40000:
    #         temp_list.append("Purple Go")
    #     else:
    #         temp_list.append("Null")

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