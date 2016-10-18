from PIL import Image
from time import time

def findOrange(img):
    t0 = time()
    width, height = img.size
    pic = img.load()
    mostOrange = 1
    previousTally = 0
    currentTally = 0

    #Top Left
    for x in range (0,width/3):
        for y in range (0,height/3):
            r, g, b, a = img.getpixel((x,y))
            if r > 254 and r < 256 and g > 164 and g < 166 and b > -1 and b < 1:
                currentTally = currentTally + 1
    previousTally = currentTally
    
    #Top Center
    currentTally = 0
    for x in range (width/3,width/2):
        for y in range (0,height/3):
            r, g, b, a = img.getpixel((x,y))
            if r > 254 and r < 256 and g > 164 and g < 166 and b > -1 and b < 1:
                currentTally = currentTally + 1
    if currentTally > previousTally:
        mostOrange = 2
    previousTally = currentTally

    #Top Right
    currentTally = 0
    for x in range (width/2,width):
        for y in range (0,height/3):
            r, g, b, a = img.getpixel((x,y))
            if r > 254 and r < 256 and g > 164 and g < 166 and b > -1 and b < 1:
                currentTally = currentTally + 1
    if currentTally > previousTally:
        mostOrange = 3
    previousTally = currentTally

    #Left
    currentTally = 0
    for x in range (0,width/3):
        for y in range (height/3,height/2):
            r, g, b, a = img.getpixel((x,y))
            if r > 254 and r < 256 and g > 164 and g < 166 and b > -1 and b < 1:
                currentTally = currentTally + 1
    if currentTally > previousTally:
        mostOrange = 4
    previousTally = currentTally

    #Center
    currentTally = 0
    for x in range (width/3,width/2):
        for y in range (height/3,height/2):
            r, g, b, a = img.getpixel((x,y))
            if r > 254 and r < 256 and g > 164 and g < 166 and b > -1 and b < 1:
                currentTally = currentTally + 1
    if currentTally > previousTally:
        mostOrange = 5
    previousTally = currentTally

    #Right
    currentTally = 0
    for x in range (width/2,width):
        for y in range (height/3,height/2):
            r, g, b, a = img.getpixel((x,y))
            if r > 254 and r < 256 and g > 164 and g < 166 and b > -1 and b < 1:
                currentTally = currentTally + 1
    if currentTally > previousTally:
        mostOrange = 6
    previousTally = currentTally

    #Bottom Left
    currentTally = 0
    for x in range (0,width/3):
        for y in range (height/2,height):
            r, g, b, a = img.getpixel((x,y))
            if r > 254 and r < 256 and g > 164 and g < 166 and b > -1 and b < 1:
                currentTally = currentTally + 1
    if currentTally > previousTally:
        mostOrange = 7
    previousTally = currentTally

    #Bottom Center
    currentTally = 0
    for x in range (height/3,height/2):
        for y in range (height/2,height):
            r, g, b, a = img.getpixel((x,y))
            if r > 254 and r < 256 and g > 164 and g < 166 and b > -1 and b < 1:
                currentTally = currentTally + 1
    if currentTally > previousTally:
        mostOrange = 8
    previousTally = currentTally

    #Bottom Right
    currentTally = 0
    for x in range (height/2,height):
        for y in range (height/2,height):
            r, g, b, a = img.getpixel((x,y))
            if r > 150 and r < 300 and g > 100 and g < 200 and b > -50 and b < 50:
                currentTally = currentTally + 1
    if currentTally > previousTally:
        mostOrange = 9
    previousTally = currentTally

    #Return the sector with the most orange
    print mostOrange
    t1 = time()
    print t1-t0
    return mostOrange 

#Where the code starts
img = Image.open('test2.png')
command = findOrange(img)

#Notes
#500 x 500 pixel image takes an average: .44 seconds to complete
#2 images per second
#300 x 300 pixel image takes an average: .15 seconds to complete
#6-7 images per second


                
    
