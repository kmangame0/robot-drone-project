#!/usr/bin/env python
# 
# Released under the BSD license. See LICENSE file for details.
"""
This program basically does face detection an blurs the face out.
"""
print __doc__

from SimpleCV import *

# Initialize the camera
cam = Camera(prop_set={'width':600,'height':480})

# Create the display to show the image
display = Display()

# Haar Cascade face detection, only faces
#haarcascade = HaarCascade("haarcascade_upperbody.xml")
haarcascade = HaarCascade("haarcascade_profileface.xml")



# Loop forever
while display.isNotDone():
    # Get image, flip it so it looks mirrored, scale to speed things up
    img = cam.getImage().flipHorizontal().scale(0.5)
    # Load in trained face file
    faces = img.findHaarFeatures(haarcascade)
    #hands = img.findHaarFeatures(handcascade)
    # Pixelize the detected face
    if faces:
        face = faces[-1]
        face.draw(Color.RED,1)
##    if hands:
##        hand = hands[-1]
##        hand.draw(Color.BLUE,1)
    # Display the image
    img.show()
