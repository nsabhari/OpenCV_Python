'''
This code is to rotate nad scaling a image in OpenCV using Affline Transform. This is based on OpenCV Tutorial.
Author: Sabhari Natarajan

Translation can also be done using Affline Transform
'''

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('Test_Sudoku_1.jpg')
rows,cols,h = img.shape
cv2.namedWindow('ROTATION',0)
cv2.resizeWindow('ROTATION',1080,720)
cv2.createTrackbar('Rotation Angle','ROTATION',0,360,nothing)
cv2.createTrackbar('Scale x 10','ROTATION',1,50,nothing)

k = 0
while(k!=27):
    rot = cv2.getTrackbarPos('Rotation Angle','ROTATION')
    scale = (cv2.getTrackbarPos('Scale x 10','ROTATION'))/10.0

    #cv2.getRotationMatrix2D(Centre,Angle,Scale)
    M = cv2.getRotationMatrix2D((cols/2,rows/2),rot,scale)
    res = cv2.warpAffine(img,M,(cols,rows))

    scale = min(1080.0/res.shape[0],720.0/res.shape[1])
    res = cv2.resize(res,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
     
    cv2.imshow('ROTATION',res)
    k = cv2.waitKey(1)
    
cv2.startWindowThread()
cv2.destroyAllWindows()
