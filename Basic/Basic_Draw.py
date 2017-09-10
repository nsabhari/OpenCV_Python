'''
This code is based on the OpenCV Tutorial for drawing a circle/line/text on a image
Author: Sabhari Natarajan
'''

import numpy as np
import cv2

# BGR mode in python

#Creating a black image with screen size i.e. 512 x 512 pix , RGB i.e.3
img = np.zeros((512,512,3), np.uint8)

cv2.line(img,(0,255),(255,0),(255,0,0),5)           # file,start,end,color,thickness
cv2.rectangle(img, (384,0),(510,128),(0,255,0),-1)  # top-left and right-bottom
cv2.circle(img,(447,63),63,(0,0,255), -1)           # centre co-ordinates , radius
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

cv2.imshow('RESULT',img)
cv2.waitKey(0)
cv2.startWindowThread()
cv2.destroyAllWindows()
