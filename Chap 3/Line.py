# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:41:56 2018

@author: MSI
"""

import numpy as np
import cv2

img = cv2.imread('Lenna.jpg',cv2.IMREAD_COLOR)

cv2.line(img , (0,0),(50,50),(255,255,255),10)

cv2.rectangle(img, (20,20),(200,200), (0,0,0),15)

cv2.circle(img, (300,300),50,(255,0,0),10,-1)



font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img , 'LENNA',(250,100),font,2,(200,100,50),2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()