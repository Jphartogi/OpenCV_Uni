# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 13:52:39 2018

@author: Hexidaz
"""

import cv2 as cv

img = cv.imread('D:\Document\Spyder Project\Images\eidolon.jpg')
img = cv.resize(img, (1600, 900))

ret,thresh1 = cv.threshold(img, 128, 255, cv.THRESH_BINARY)
cv.imshow('Binary Thresholding', thresh1)
ret,thresh2 = cv.threshold(img, 128, 255, cv.THRESH_BINARY_INV)
cv.imshow('Binary Inverse Thresholding', thresh2)
ret,thresh3 = cv.threshold(img, 128, 255, cv.THRESH_TRUNC)
cv.imshow('Trunc Thresholding', thresh3)
ret,thresh4 = cv.threshold(img, 128, 255, cv.THRESH_TOZERO_INV)
cv.imshow('Tozero Inverse Thresholding', thresh4)
ret,thresh5 = cv.threshold(img, 128, 255, cv.THRESH_TOZERO)
cv.imshow('Tozero Thresholding', thresh5)

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thresh1_a = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 5)
cv.imshow('Binary Adaptive Thresholding 1a', thresh1_a)
thresh2_a = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 7, 5)
cv.imshow('Binary Adaptive Thresholding 2a', thresh2_a)
print 'Cannot use other method as it is stated in the website the Thereshold method MUST be cv2.THRESH_BINARY or cv2.THRESH_BINARY_INV, and I also tried and eded up in a crash'

thresh1_b = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 0)
cv.imshow('Binary Adaptive Thresholding 1b', thresh1_b)
thresh2_b = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 7, 0)
cv.imshow('Binary Adaptive Thresholding 2b', thresh1_b)
print 'Cannot use other method as it is stated in the website the Thereshold method MUST be cv2.THRESH_BINARY or cv2.THRESH_BINARY_INV, and I also tried and eded up in a crash'

thresh1_c = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, -5)
cv.imshow('Binary Adaptive Thresholding 1c', thresh1_c)
thresh2_c = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 7, -5)
cv.imshow('Binary Adaptive Thresholding 2c', thresh1_c)
print 'Cannot use other method as it is stated in the website the Thereshold method MUST be cv2.THRESH_BINARY or cv2.THRESH_BINARY_INV, and I also tried and eded up in a crash'

cv.waitKey(0)
cv.destroyAllWindows()