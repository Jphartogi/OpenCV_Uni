# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:44:38 2018

@author: MSI
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame by frame
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    template = cv2.imread('face.jpg',0)
    w,h = template.shape[::-1]

    res = cv2.matchTemplate(gray,template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.4
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame,pt,(pt[0]+w,pt[1]+h),(0,255,200),2)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('detected',frame)
      

cap.release()
cv2.destroyAllWindows()



