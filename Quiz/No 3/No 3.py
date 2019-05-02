# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:31:41 2018

@author: MSI
"""

import cv2
import numpy as np

src1 = cv2.imread("img1.jpg")
src2 = cv2.imread("img2.jpg")

#a
src1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
src2 = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
diff12 = src1 - src2

kernel = np.ones((6,6),np.uint8)
opening = cv2.morphologyEx(diff12, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(diff12, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Source1', src1)
cv2.imshow('Source2',src2)
cv2.imshow('Substract result', diff12)
cv2.imwrite('subs_result.jpg',diff12)

cv2.imshow('cleanDiff', opening)
cv2.imwrite('cleandiff.jpg',opening)
cv2.imshow('dirtyDiff', closing)
cv2.imwrite('dirtydiff.jpg',closing)
cv2.waitKey(0)
cv2.destroyAllWindows(0)

'''
dirtydiff is removing the noise and turn it into white color, while the clean diff is
turning noise into the black colour. 

while the opening is the process erode followe by dilate
while the closing is dilate followed by erode

'''