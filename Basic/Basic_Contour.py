'''
This code is to see the effect of varying Canny Edge parameters.
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
    
img = cv2.imread('Test_Road.jpg')

def Create_Trackbar():
    cv2.namedWindow('PARAMETERS',0)
    cv2.createTrackbar('Min Intensity Gradient','PARAMETERS',0,900,nothing)
    cv2.createTrackbar('Max Intensity Gradient','PARAMETERS',0,900,nothing)
    cv2.createTrackbar('Aperture Size','PARAMETERS',3,7,nothing)
    cv2.resizeWindow('PARAMETERS',600,100)
    cv2.moveWindow('PARAMETERS',10,10)

Create_Trackbar()
img = cv2.medianBlur(img,5)
contour = img.copy()
k= 0

while(k!=27):
    mina = cv2.getTrackbarPos('Min Intensity Gradient','PARAMETERS')
    maxa = cv2.getTrackbarPos('Max Intensity Gradient','PARAMETERS')
    size = cv2.getTrackbarPos('Aperture Size','PARAMETERS')
    if size%2 == 0: size=size-1
    if size < 3 :   size = 3

    canny = cv2.Canny(img,mina,maxa,L2gradient=True,apertureSize = size)
    contours, hierarchy = cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contour = img.copy()
    # cv2.drawContours(File to be saved, contours, its number (-1 for all), color, thickness)
    cv2.drawContours(contour,contours ,-1, (0,0,255), -1)
    res = np.concatenate((img,cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR),contour),axis=1)
    scale = min(1080.0/res.shape[0],720.0/res.shape[1])
    res = cv2.resize(res,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
    
    cv2.imshow('RESULT',res)
    k = cv2.waitKey(1) & 0xFF

cv2.startWindowThread()
cv2.destroyAllWindows()
