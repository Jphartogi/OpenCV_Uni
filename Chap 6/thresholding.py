# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 22:10:48 2018

@author: MSI
"""

import cv2

img= cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img,10,255,cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,2)
gaus2 = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,35,2)

Hist = cv2.equalizeHist(grayscaled)

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('grayscaled',grayscaled)

cv2.imshow('ORIGINAL',img)
cv2.imshow('GAUS',gaus)
cv2.imshow('GAUS2',gaus2)
cv2.imshow('HIST',Hist)
cv2.waitKey(0)
cv2.destroyAllWindows()
