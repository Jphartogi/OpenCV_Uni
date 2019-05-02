# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:41:08 2018

@author: MSI
"""

import cv2 
import numpy as np

img1 = cv2.imread('machine.jpg')
img2 = cv2.imread('opencv-logo2.png')

img3 = cv2.resize(img1,(300,300))
img4 = cv2.resize(img2,(300,300))

dst = cv2.addWeighted(img3,0.7,img4,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()