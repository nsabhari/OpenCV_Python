'''
This code is to see use of contours. This is based on the OpenCV Tutorial.
Author: Sabhari Natarajan

The various parameters can be varied using the trackbar.
The results are shown in one single image in the order
    'ORIGINAL'  'AFTER CANNY EDGE'  'AFTER CONTOUR'
'''

import cv2
import numpy as np

def nothing(x):
    pass    
    
img = cv2.imread('Test_Contour.jpg')

def Create_Trackbar():
    cv2.namedWindow('CONTOUR',0)
    cv2.createTrackbar('Min Intensity Gradient','CONTOUR',0,900,nothing)
    cv2.createTrackbar('Max Intensity Gradient','CONTOUR',0,900,nothing)
    cv2.createTrackbar('Aperture Size','CONTOUR',3,7,nothing)
    cv2.resizeWindow('CONTOUR',1080,720)

Create_Trackbar()
img = cv2.medianBlur(img,5)
contour = img.copy()
k= 0

while(k!=27):
    mina = cv2.getTrackbarPos('Min Intensity Gradient','CONTOUR')
    maxa = cv2.getTrackbarPos('Max Intensity Gradient','CONTOUR')
    size = cv2.getTrackbarPos('Aperture Size','CONTOUR')
    if size%2 == 0: size=size-1
    if size < 3 :   size = 3

    canny = cv2.Canny(img,mina,maxa,L2gradient=True,apertureSize = size)
    contours, hierarchy = cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contour = img.copy()
    # cv2.drawContours(File to be saved, Variable in which contours were saved, its number (-1 for all), color, thickness)
    '''
    NOTE: IF THERE ARE TOO MANY CONTOURS TO BE DRAWN THE CODE MIGHT CRASH.
    Reduxe the number of contours either by changing the params for Canny or delete the unwanted Contours based on Length or Area.
    There may be other ways also.
    U may also choose to draw only specific contours instead of all.
    '''
    cv2.drawContours(contour,contours ,-1, (0,0,255), -1)
    res = np.concatenate((img,cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR),contour),axis=1)
    scale = min(1080.0/res.shape[0],720.0/res.shape[1])
    res = cv2.resize(res,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
    
    cv2.imshow('CONTOUR',res)
    k = cv2.waitKey(1)

cv2.startWindowThread()
cv2.destroyAllWindows()
