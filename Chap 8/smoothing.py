# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:25:00 2018

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
    kernel = np.ones((15,15), np.float32)/125
    smoothed = cv2.filter2D(res,-1,kernel)
    blur = cv2.GaussianBlur(res,(15,15),0)
    median = cv2.medianBlur(res,15)
    bilateral = cv2.bilateralFilter(res,15,75,75)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    cv2.imshow('bilateral',bilateral)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()    
cv2.destroyAllWindows()

