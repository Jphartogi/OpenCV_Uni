# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 20:32:04 2018

@author: MSI
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
 
while (True):
    _, frame = cap.read()
       
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    sobely = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)#IN HORIZONTAL
    sobelx = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)#IN VERTICAL
    canny = cv2.Canny(frame,140,220)
    
    
    cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('canny',canny)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()    
cv2.destroyAllWindows()
