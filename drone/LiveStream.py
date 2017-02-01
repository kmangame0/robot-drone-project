import Tkinter as tk
from SimpleCV import *
from PIL import Image, ImageTk

w=640
h=320

#640 x 320 works good

cam = Camera(0,{"width":w,"height":h})
disp = Display()
root = tk.Tk()
lmain = tk.Label(root)
lmain.pack()
root.title("Autonomous Robot Control Center")
root.geometry("1280x720")
js = JpegStreamer("0.0.0.0:8080",0.005)
print(js.url())
print(js.streamUrl())

while disp.isNotDone():
    img = cam.getImage()
    img.show()
    img.save(js)
