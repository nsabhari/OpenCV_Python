'''
This codes helps to test or extract the HSV range for masking a color from a video feed
Author: Sabhari Natarajan

Directions to use:
1) Set "Name" to the required value.
2) Vary the HSV Range from the trackbar.
3) Pressing 'p' will pause the video but the masking action continues i.e. you can continue selecting the pixels.
4) Press 'r' to reset the HSV range to initial value
5) Press "Esc" when you are done. The results will be printed in the Shell

The input frame is shown in the "ORIGINAL" window and masked result in the "RESULT" window.
You can select the pixels only form the "ORIGINAL" window
'''

import numpy as np
import cv2

def nothing(x):
    pass

def Create_Trackbar():
    cv2.namedWindow('HSV RANGES')
    cv2.resizeWindow('HSV RANGES',400,200)
    cv2.createTrackbar('Low_Hue','HSV RANGES',0,179,nothing)
    cv2.createTrackbar('High_Hue','HSV RANGES',0,179,nothing)
    cv2.createTrackbar('Low_Sat','HSV RANGES',0,255,nothing)
    cv2.createTrackbar('High_Sat','HSV RANGES',0,255,nothing)
    cv2.createTrackbar('Low_Val','HSV RANGES',0,255,nothing)
    cv2.createTrackbar('High_Val','HSV RANGES',0,255,nothing)

'''
Set Name to the video file name you want to use Eg: "Test_Video.mp4"
If is a camera then set Name to 0 or 1         Eg: 0
'''
Name = 0
cap = cv2.VideoCapture(Name)
Low_HSV = [0,0,0]
High_HSV = [179,255,255]
kernel = np.ones((3,3),np.uint8)
k = 0
Pause = False

Create_Trackbar()

while(k!=27):
    Low_HSV[0] = cv2.getTrackbarPos('Low_Hue','HSV RANGES')
    Low_HSV[1] = cv2.getTrackbarPos('Low_Sat','HSV RANGES')
    Low_HSV[2] = cv2.getTrackbarPos('Low_Val','HSV RANGES')
    High_HSV[0] = cv2.getTrackbarPos('High_Hue','HSV RANGES')
    High_HSV[1] = cv2.getTrackbarPos('High_Sat','HSV RANGES')
    High_HSV[2] = cv2.getTrackbarPos('High_Val','HSV RANGES')
    if Pause == False:
        # Take each frame
        ret, frame = cap.read()
        if ret == False:
            cap = cv2.VideoCapture(Name)
            ret, frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    # Thresholding using HSV ranges
    mask = cv2.inRange(hsv, np.array(Low_HSV), np.array(High_HSV))
    mask = cv2.dilate(mask,kernel,iterations = 2)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('ORIGINAL',frame)
    cv2.imshow('RESULT',res)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('p'):
        Pause = not Pause
        
cap.release()
print "Low HSV Limit : ", Low_HSV, "\nHigh HSV Limit : ",High_HSV
cv2.startWindowThread()
cv2.destroyAllWindows()
