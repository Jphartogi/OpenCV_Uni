# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:27:50 2018

@author: MSI
"""

import cv2
import numpy as np

img = cv2.imread('traffic.jpg')
rows2,cols2,channels2 = img.shape

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
px = hsv[110,35]
print px

    
lower_red = np.array([160,210,200])
upper_red = np.array([180,240,255])


    
mask = cv2.inRange(hsv,lower_red, upper_red)
res = cv2.bitwise_and(img,img, mask = mask) ##bitwise-> where there is something in the frame and mask is true
                                                    ## mask is in range of lower red, upper red. if in the range = true.
cv2.imshow('hsv',hsv)
cv2.imshow('frame',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
    
   
cv2.waitKey(0)    
cv2.destroyAllWindows()


