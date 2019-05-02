# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 11:40:07 2018

@author: MSI
"""

import cv2
import numpy as np

img = cv2.imread('scene.jpg')
#a
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel = np.ones((9,9),np.uint8)
tophat = cv2.morphologyEx(grayscale, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('scene',img)
cv2.imshow('grayscaled',grayscale)
cv2.imshow('tophat',tophat)
#b

ret, mask = cv2.threshold(tophat,10,255,cv2.THRESH_BINARY_INV)

#c
gray_value = np.full(tophat.shape,255) #assuming grayscale value
sum_img = cv2.add(tophat,gray_value)

cv2.imshow('mask',mask)
cv2.imshow('sum_img',sum_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

