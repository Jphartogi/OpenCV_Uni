# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 12:19:43 2018

@author: MSI
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img= cv2.imread('cameraman.png',0)
retval, threshold = cv2.threshold(img,10,255,cv2.THRESH_BINARY)

grayscaled = img
retval, threshold2 = cv2.threshold(grayscaled, 40, 255, cv2.THRESH_BINARY)
#Gaussian
gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,2)

#Mean
mean = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2)


# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in xrange(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
Hist = cv2.equalizeHist(grayscaled)

cv2.imshow('threshold2',threshold2)

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)

cv2.imshow('grayscaled',grayscaled)
cv2.imshow('OTSU1',th2)
cv2.imshow('OTSU2',th3)
cv2.imshow('GAUS',gaus)
cv2.imshow('MEAN',mean)
cv2.imshow('HIST',Hist)

cv2.waitKey(0)
cv2.destroyAllWindows()
