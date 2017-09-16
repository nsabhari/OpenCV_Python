'''
This code is to see the effect of various types of blur in a image. This is based on the OpenCV tutorial.
Author: Sabhari Natarajan

The kernel size can be varied using the trackbar.
The results are shown in one single image in the order
    'ORIGINAL'          '2D CONVOLUTION'    'AVERAGING'
    'GAUSSIAN BLUR'     'MEDIAN BLUR'       'ORIGINAL'
'''

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('Test_Lena.png')
cv2.namedWindow('BLUR',1)
cv2.createTrackbar('Kernel','BLUR',2,20,nothing)
cv2.resizeWindow('BLUR',1080,720)
k = 0

while(k!=27):
    x = cv2.getTrackbarPos('Kernel','BLUR')
    if x<2: x=2
    kernel = np.ones((x,x),np.float32)/(x**2)
    Convolution_2D = cv2.filter2D(img,-1,kernel)
    Averaging = cv2.blur(img,(x,x))
    if x%2 == 0:    x = x - 1
    Gauss_Blur = cv2.GaussianBlur(img,(x,x),0)
    if x < 3:   x=3
    Median = cv2.medianBlur(img,x)

    res_a = np.concatenate((img,Convolution_2D,Averaging),axis = 1)
    res_b = np.concatenate((Gauss_Blur,Median,img),axis = 1)
    res = np.concatenate((res_a,res_b),axis = 0)
    scale = min(1080.0/res.shape[0],720.0/res.shape[1])
    res = cv2.resize(res,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('BLUR',res)
       
    k = cv2.waitKey(1) & 0xFF

cv2.startWindowThread()
cv2.destroyAllWindows()
