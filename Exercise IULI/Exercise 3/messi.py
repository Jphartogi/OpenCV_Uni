# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:28:19 2018

@author: MSI
"""

import cv2
import numpy as np

img= cv2.imread('messi.jpg')
rows,cols,colloumns = img.shape


ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
'''
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
'''
cv2.imshow('messi',img)
cv2.waitKey(0)
cv2.destroyAllWindows()