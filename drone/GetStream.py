from SimpleCV import *
from Tkinter import Tk, Label
import time
import numpy as numpy
from PIL import Image, ImageTk

root = Tk()
root.title("Autonomous Flight Control Center")
root.geometry("800x600")  
lmain = Label(root)
lmain.pack() 
cam = JpegStreamCamera("http://141.209.170.195:8080/stream") 

def show_frame():
    global lmain
    frame = cam.getImage()
    frame.save("frame.jpg")
    #frame = Image("frame.jpg")
    frame = cv2.imread('frame.jpg')
    print type(frame) 
    #arr = numpy.array(frame)
    #img.show() 
    #frame = numpy.array(frame)
    #frame = np.asarray(frame[:,:])
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    print type(cv2image)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 

show_frame()
root.mainloop()