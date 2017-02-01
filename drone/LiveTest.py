
import time
from SimpleCV import *
c = Camera(0)
js = JpegStreamer("0.0.0.0:8080",0.005)  #starts up an http server (defaults to port 8080)
while True:
	c.getImage().save(js)
	time.sleep(0.1)