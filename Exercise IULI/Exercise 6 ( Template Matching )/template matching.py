# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:25:15 2018

@author: MSI
"""

import cv2
import numpy as np

img = cv2.imread('messi.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template = cv2.imread('ball.jpg',0)
w,h = template.shape[::-1]

res = cv2.matchTemplate(gray,template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow('detected',img)
cv2.imwrite('test.jpg',img)


