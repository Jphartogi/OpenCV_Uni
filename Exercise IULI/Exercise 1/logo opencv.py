# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:18:44 2018

@author: Yosaphat
"""

import numpy as np
import cv2

red = (0,0,255)
blue = (255,0,0)
green = (0,255,0)
white = (255,255,255)
yellow = (0,255,255)
ang = 90


img = np.ones((600,600,3),np.uint8)
img[:] = [255,255,255]
cv2.circle(img, (300,300),100,(0,0,0),80,-1)
cv2.circle(img,(300,300),150,(0,0,0),5)
cv2.circle(img,(300,300),70,(255,255,255),40,-1)
cv2.ellipse(img,(300,300),(80,80),2*ang,0,90,(120,0,0),-1)
cv2.ellipse(img,(300,300),(80,80),4*ang,0,90,(120,0,0),-1)


cv2.imshow('img',img)
cv2.imwrite('bmw.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
