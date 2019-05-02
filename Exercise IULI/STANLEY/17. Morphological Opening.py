# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 13:52:39 2018

@author: Hexidaz
"""

import cv2
import numpy as np

background = cv2.imread('D:\Document\Spyder Project\Images\WIN_20180310_17_33_09_Pro.jpg')
foreground = cv2.imread('D:\Document\Spyder Project\Images\WIN_20180310_17_33_19_Pro.jpg')

bg_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
fg_gray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)

def diff(img,img1): # returns just the difference of the two images
  return cv2.absdiff(img,img1)

def diff_remove_bg(img0,img,img1): # removes the background but requires three images 
  d1 = diff(img0,img)
  d2 = diff(img,img1)
  return cv2.bitwise_and(d1,d2)

absimg = diff(bg_gray, fg_gray)
cv2.imshow('Absolute Difference', absimg)

_, bin_thres = cv2.threshold(absimg, 50, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Thresholding', bin_thres)

kernel = np.ones((2,2),np.uint8)
opening = cv2.morphologyEx(bin_thres, cv2.MORPH_OPEN, kernel)
cv2.imshow('CV_MOP_OPEN', opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
