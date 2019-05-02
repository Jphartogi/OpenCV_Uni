# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 13:38:48 2018

@author: MSI
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
 
while (True):
    ret, frame = cap.read()
    grayscaled = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   
    canny = cv2.Canny(frame,140,220)
    numpy_horizontal = np.hstack((grayscaled,canny))
    numpy_horizontal_concat = np.concatenate((grayscaled,canny), axis=1)

    
    cv2.imshow('original',frame)
    cv2.imshow('grayscaled',grayscaled)
    cv2.imshow('canny',canny)
    cv2.imshow('one_window',numpy_horizontal_concat)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
     
cap.release()    
cv2.destroyAllWindows()