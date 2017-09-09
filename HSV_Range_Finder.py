'''
This codes helps to find the HSV range for masking a color from a video feed
Author: Sabhari Natarajan

Directions to use:
1) Set "Name" to the required value.
2) Choose the pixels you want to mask by holding ALT and moving your mouse over that area.
   Release ALT to stop selecting.
3) Pressing 'p' will pause the video but the masking action continues i.e. you can continue selecting the pixels.
4) Press 'r' to reset the HSV range to initial value
5) Press "Esc" when you are done. The results will be printed in the Shell

The input frame is shown in the "ORIGINAL" window and masked result in the "RESULT" window.
You can select the pixels only form the "ORIGINAL" window
'''

import numpy as np
import cv2

'''
Set Name to the video file name you want to use Eg: "Test_Video.mp4"
If is a camera then set Name to 0 or 1         Eg: 0
'''
Name = 0
cap = cv2.VideoCapture(Name)
Low_HSV = [179,255,255]
High_HSV = [0,0,0]
kernel = np.ones((3,3),np.uint8)
k = 0
Pause = False

def find_hsv(event,x,y,flags,param):
    if (event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_ALTKEY):
        global Low_HSV, High_HSV
        px = np.uint8([[frame[y,x]]])
        hsv = cv2.cvtColor(px,cv2.COLOR_BGR2HSV)
        hsv = [hsv[0,0,0],hsv[0,0,1],hsv[0,0,2]]
        for i in range(0,3):
            Low_HSV[i] = min(Low_HSV[i],hsv[i])
            High_HSV[i] = max(High_HSV[i],hsv[i])
                    
_, frame = cap.read()
cv2.imshow('ORIGINAL',frame)
cv2.setMouseCallback('ORIGINAL',find_hsv)

while(k!=27):
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
    elif k == ord('r'):
        print "HSV Range Reset Done"
        Low_HSV = [179,255,255]
        High_HSV = [0,0,0]
        
cap.release()
print "Low HSV Limit : ", Low_HSV, "\nHigh HSV Limit : ",High_HSV
cv2.startWindowThread()
cv2.destroyAllWindows()

