'''
This code is to see the effect of varying Canny Edge parameters.This is based on the OpenCV Tutorial.
Author: Sabhari Natarajan

The various parameters can be varied using the trackbar.
The results are shown in one single image in the order
    'ORIGINAL'  'AFTER CANNY EDGE'

It is always better to use Canny Edge after masking or thresholding.
This code has Canny Edge only though.
'''

import cv2
import numpy as np

def nothing(x):
    pass    
    
img = cv2.imread('Test_Contour.jpg',0)

def Create_Trackbar():
    cv2.namedWindow('CANNY EDGE',0)
    cv2.createTrackbar('Min Intensity Gradient','CANNY EDGE',0,900,nothing)
    cv2.createTrackbar('Max Intensity Gradient','CANNY EDGE',0,900,nothing)
    cv2.createTrackbar('Aperture Size','CANNY EDGE',3,7,nothing)
    cv2.resizeWindow('CANNY EDGE',1080,720)
    
Create_Trackbar()
img = cv2.medianBlur(img,5)
k= 0

while(k!=27):
    mina = cv2.getTrackbarPos('Min Intensity Gradient','CANNY EDGE')
    maxa = cv2.getTrackbarPos('Max Intensity Gradient','CANNY EDGE')
    size = cv2.getTrackbarPos('Aperture Size','CANNY EDGE')
    if size%2 == 0: size=size-1
    if size < 3 :   size = 3

    canny = cv2.Canny(img,mina,maxa,L2gradient=True,apertureSize = size)
    res = np.concatenate((img,canny),axis=1)
    scale = min(1080.0/res.shape[0],720.0/res.shape[1])
    res = cv2.resize(res,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
    
    cv2.imshow('CANNY EDGE',res)
    k = cv2.waitKey(1) & 0xFF

cv2.startWindowThread()
cv2.destroyAllWindows()
    
    
