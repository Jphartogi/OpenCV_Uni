# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:03:30 2018

@author: MSI
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
 
while (True):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,40,0])
    upper_red = np.array([50,200,255])
    
    mask = cv2.inRange(hsv,lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask = mask) ##bitwise-> where there is something in the frame and mask is true
                                                    ## mask is in range of lower red, upper red. if in the range = true.
                                                    
    kernel = np.ones((5,5), np.uint8)  #uint8= unsigned integer = from 0 to 255
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations= 1)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    
    
    
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('closing',closing)
    cv2.imshow('opening',opening)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()    
cv2.destroyAllWindows()