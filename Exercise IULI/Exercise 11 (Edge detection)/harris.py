# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 12:40:41 2018

@author: MSI
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('simple2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,40,0.05,30)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()