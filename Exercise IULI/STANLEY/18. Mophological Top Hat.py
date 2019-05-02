# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 18:06:55 2018

@author: Hexidaz
"""

import cv2
import numpy as np

img = cv2.imread('SHELTER.jpg')
img = cv2.resize(img, (1024, 576))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img_gray, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('Tophat', tophat)

ret, mask = cv2.threshold(tophat, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('Mask', mask)

add = cv2.add(tophat, mask)
cv2.imshow('Add', add)

cv2.waitKey(0)
cv2.destroyAllWindows()