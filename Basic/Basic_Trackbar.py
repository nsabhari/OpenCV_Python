'''
This code shows how to use the trackbar to change variables during runtime. This is based on the OpenCV tutorial.
Author: Sabhari Natarajan
'''

import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('RGB Variation',0)
cv2.resizeWindow('RGB Variation',1080,720)

# create trackbars for color change
#cv2.createTrackbar(Trackbar Name, Window Name, Min, Max, Function name that is called)
cv2.createTrackbar('R','RGB Variation',0,255,nothing)
cv2.createTrackbar('G','RGB Variation',0,255,nothing)
cv2.createTrackbar('B','RGB Variation',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'RGB Variation',0,1,nothing)

k = 0

while(k!=27):
    cv2.imshow('RGB Variation',img)
    k = cv2.waitKey(1)

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','RGB Variation')
    g = cv2.getTrackbarPos('G','RGB Variation')
    b = cv2.getTrackbarPos('B','RGB Variation')
    s = cv2.getTrackbarPos(switch,'RGB Variation')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.startWindowThread()
cv2.destroyAllWindows()
