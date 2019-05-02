# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 23:28:07 2018

@author: MSI
"""

import cv2

img = cv2.imread('Lenna.jpg',cv2.IMREAD_COLOR)

px = img[55,55]

img [100:200, 300:400] = [255,255,255]

cutface = img[200:400,220:400]
img[0:200,0:180] = cutface

cv2.imshow('image',img,)
cv2.waitKey(0)
cv2.destroyAllWindows()