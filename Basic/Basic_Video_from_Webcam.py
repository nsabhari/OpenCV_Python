'''
This code is to read a video file/ capture a live feed and save the video to another file. This is based on the OpenCV
tutorial.
Author: Sabhari Natarajan
'''

import numpy as np
import cv2
from time import time

cap = cv2.VideoCapture(0)
if cap.isOpened() == 0:
    print "OPENING VIDEO FILE ERROR"
    exit()
    
''' Use this to get stream from a feed coming from a network:    
    cap.open("http://192.168.43.1:8080//video?.mjpeg")

    To open a saved file:
    cv2.VideoCapture("Test_File.mp4")
    Mention the file directory if needed.
'''
'''
    Various camera parameters like width, height and fps can be set using cap.set().
    Check the API reference for more details
'''
# This is to save the video
Save_Video = 0
if Save_Video == 1:
    fourcc = cv2.cv.CV_FOURCC('D','I','V','X')
    #cv2.VideoWriter(Output FIle Name, format, fps, size) : Size is in (cols, rows)
    out = cv2.VideoWriter('OUTPUT.avi',fourcc, 12.8, (int(cap.get(3)),int(cap.get(4))))
'''NOTE: fps will not be always 30.0. It depends on your system and code
   Here fps is more like the fps at which it saves the frames to the file.
   So if your PC is slow then if webcam sends at x fps then the actual fps in the code will be much less than that.

   This is only if you record from a live feed.
   If you are playing a previously recorded file then use the fps of that file itself.

   You can find the fps of a live feed by creating a OpenCV code for that or using 3rd party softwares.
'''

k = 0

while(k!=27):
    ret, frame = cap.read()
    cv2.imshow('FRAME',frame)
    if Save_Video == 1:  out.write(frame)    
    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite("Capture.jpg",frame)
        print 'PHOTO TAKEN'

cap.release()
if Save_Video == 1:  out.release()
cv2.startWindowThread()
cv2.destroyAllWindows()
