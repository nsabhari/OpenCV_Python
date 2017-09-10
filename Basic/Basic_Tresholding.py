'''
This code is to see the effect of various types of thresholding in a image
Author: Sabhari Natarajan

The various parameters can be varied using the trackbar.
The results are shown in one single image in the order
    'ORIGINAL'          'NORMAL THRESHOLDING'               'AFTER DILATION'
    'ORIGINAL'          'ADAPTIVE MEAN THRESHOLDING'        'AFTER DILATION'
    'ORIGINAL'          'ADAPTIVE GAUSSIAN THRESHOLDING'    'AFTER DILATION'
'''

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('Test_Road.jpg',0)

def Create_Trackbar():
    cv2.namedWindow('PARAMETERS',0)
    cv2.resizeWindow('PARAMETERS',500,100)
    cv2.createTrackbar('Threshold Value(A)','PARAMETERS',0,255,nothing)
    cv2.createTrackbar('NEIGHBOUR SIZE(B,C)','PARAMETERS',3,99,nothing)
    cv2.createTrackbar('SUBTRACTING CONSTANT(B,C)','PARAMETERS',1,20,nothing)
    cv2.createTrackbar('Kernel Size','PARAMETERS',2,20,nothing)
    cv2.createTrackbar('Iterations','PARAMETERS',1,20,nothing)
    
Create_Trackbar()
img = cv2.medianBlur(img,5)
k= 0

while(k!=27):
    Threshold_Value = cv2.getTrackbarPos('Threshold Value(A)','PARAMETERS')
    Kernel_Size = cv2.getTrackbarPos('Kernel Size','PARAMETERS')
    Iter = cv2.getTrackbarPos('Iterations','PARAMETERS')
    if Iter<1:  Itera = 1
    if Kernel_Size<1:   Kernel_Size=1
    kernel = np.ones((Kernel_Size,Kernel_Size),np.uint8)
    pix = cv2.getTrackbarPos('NEIGHBOUR SIZE(B,C)','PARAMETERS')
    if pix%2 == 0:  pix = pix - 1
    if pix < 3: pix = 3
    c = cv2.getTrackbarPos('SUBTRACTING CONSTANT(B,C)','PARAMETERS')
    ret,th1 = cv2.threshold(img,Threshold_Value,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,pix,c)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,pix,c)

    res_a = np.concatenate((img,th1,cv2.dilate(th1,kernel,iterations = Iter)),axis = 1)
    res_b = np.concatenate((img,th2,cv2.dilate(th2,kernel,iterations = Iter)),axis = 1)
    res_c = np.concatenate((img,th3,cv2.dilate(th3,kernel,iterations = Iter)),axis = 1)
    res = np.concatenate((res_a,res_b,res_c),axis = 0)
    scale = min(1080.0/res.shape[0],720.0/res.shape[1])
    res = cv2.resize(res,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('RESULT',res)
    k = cv2.waitKey(1) & 0xFF

cv2.startWindowThread()
cv2.destroyAllWindows()
