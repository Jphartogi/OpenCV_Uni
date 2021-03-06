# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 23:03:21 2018

@author: MSI
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
 
while (True):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([150,100,0])
    upper_red = np.array([200,200,255])
    
    mask = cv2.inRange(hsv,lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask = mask) ##bitwise-> where there is something in the frame and mask is true
                                                    ## mask is in range of lower red, upper red. if in the range = true.
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()    
cv2.destroyAllWindows()


