# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:52:33 2018

@author: Jphartogi
"""

import cv2
import numpy as np


img1 = cv2.imread('bmw_car.jpg')
img2 = cv2.imread('bmw.jpg')

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]
rows1,cols1,channels1 = img1.shape

px = img1[100,100]
print(px)


gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(gray,220,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)


img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

dst = cv2.add(img1_bg,img2_fg)
img1[rows1-rows:rows1,cols1-cols:cols1] = dst

cv2.imshow('res',img1)
cv2.imwrite('blended_image.jpg',img1)
'''
cv2.imshow('mask',mask)
cv2.imshow('gray',gray)
cv2.imshow('maskinv',mask_inv)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()




