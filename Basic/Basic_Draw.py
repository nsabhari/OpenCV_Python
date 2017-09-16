'''
This code is based on the OpenCV Tutorial for drawing a circle/line/text on a image
Author: Sabhari Natarajan
'''

import numpy as np
import cv2

# For color OpenCV uses BGR mode instead of RGB

#Creating a black image with screen size i.e. 512 x 512 pix , RGB i.e.3
img = np.zeros((512,512,3), np.uint8)

#cv2.line(Image Name, Start, End, Color, Thickness)
cv2.line(img,(0,255),(255,0),(255,0,0),5) # Start and End in (Coloumn,Row) i.e. (x,y) format

#cv2.rectangle(Image Name, Top Left, Right Bottom, Color, Thickness)
cv2.rectangle(img, (384,0),(510,128),(0,255,0),-1)  # Thickness = -1 to fill inside the rectangle

#cv2.circle(Image Name, Centre, Radius, Color, Thickness)
cv2.circle(img,(447,63),63,(0,0,255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(Image Name,Text, Start, Font, Size, Color, Thickness)
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

cv2.imshow('DRAW',img)
cv2.waitKey(0)
cv2.startWindowThread()
cv2.destroyAllWindows()
