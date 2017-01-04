from SimpleCV import Image, Camera
import time

cam = Camera()
counter = 200
while counter < 450:
	time.sleep(750/1000)
	img = cam.getImage()
	img.save("subject" + str(counter) +".jpg")
	counter = counter + 1
