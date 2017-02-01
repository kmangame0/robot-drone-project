

import numpy as np
from PIL import Image

def normalize(arr):
    """
    Linear normalization
    http://en.wikipedia.org/wiki/Normalization_%28image_processing%29
    """
    arr = arr.astype('float')
    print "here"
    # Do not touch the alpha channel
    for i in range(3):
        minval = arr[...,i].min()
        maxval = arr[...,i].max()
        if minval != maxval:
            arr[...,i] -= minval
            arr[...,i] *= (255.0/(maxval-minval))
    return arr

def demo_normalize():
    img = Image.open("red.png").convert('RGBA')
    arr = np.array(img)
    new_img = Image.fromarray(normalize(arr).astype('uint8'),'RGBA')
    new_img.save('normalized.png')

demo_normalize()
