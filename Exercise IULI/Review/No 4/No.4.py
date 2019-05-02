# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 13:53:09 2018

@author: MSI
"""

import cv2
import numpy as np

img = cv2.imread('roof.jpg')
smooth3= cv2.GaussianBlur(img,(3,3),0)
smooth5= cv2.GaussianBlur(img,(5,5),0)
smooth9= cv2.GaussianBlur(img,(9,9),0)
smooth11= cv2.GaussianBlur(img,(11,11),0)
smooth_tw= cv2.GaussianBlur(smooth5,(5,5),0)


cv2.imshow('img',img)
cv2.imshow('smooth_3x3',smooth3)
cv2.imshow('smooth_5x5',smooth5)
cv2.imshow('smooth_9x9',smooth9)
cv2.imshow('smooth_11x11',smooth11)
cv2.imshow('smooth_5x5 twice',smooth_tw)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Gaussian filtering is done by convolving each point in the input array with 
a Gaussian kernel and then summing them all to produce the output array.
and the input array of 11x11 is so much different and wider than 5x5, and
when it's filtered for the second time, the input array also remain 5x5.
this condition applies as long the sigma is remain the same.
'''