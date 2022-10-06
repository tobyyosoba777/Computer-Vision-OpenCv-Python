# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 07:42:23 2022

@author: TOBBY
"""

import cv2
import sys

cap = cv2.VideoCapture(0) #0 is used to access your webcam's default index to read its video frame
if not cap.isOpened():
    print("Cannot Open Camera,exiting....")
    sys.exit()

while True:
    #capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Cannot receive frame. Exiting.....")
        break

    #used to convert video stream to gray format as the default reading format is in BGR
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #used to display the webcam stream in the gray format variable name
    cv2.imshow("gray", gray)

    #to keep the video stream actively waiting till a defined key is pressed
    key = cv2.waitKey(1)

    #27 is an ascii character meaning the esc key, when the escape key is pressed the video stream stops
    if key == 27:
        break
#function to close the video frame
cap.release()
cv2.destroyAllWindows()