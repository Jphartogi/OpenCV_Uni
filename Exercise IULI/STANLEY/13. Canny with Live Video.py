# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 13:20:51 2018

@author: Hexidaz
"""

import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while(1):
   _, frame = camera.read()
   
   grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
   height, width = grayscale.shape
   canny = cv.Canny(grayscale,100,200)
   
   cv.imshow("Original", frame)
   cv.imshow("Gray Scale", grayscale)
   cv.imshow("Canny", canny)
   
   grayscale = cv.cvtColor(grayscale, cv.COLOR_GRAY2BGR)
   canny = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
   
   combined = np.zeros((height,width,3),np.uint8)
   combined[0:height, 0:213] = frame[0:height, 0:213]
   combined[0:height, 214:426] = grayscale[0:height, 214:426]
   combined[0:height, 427:640] = canny[0:height, 427:640]
   cv.putText(combined,'Normal',(10,45), cv.FONT_HERSHEY_SIMPLEX, 1.65, 255, 2)
   cv.putText(combined,'Gray',(260,45), cv.FONT_HERSHEY_SIMPLEX, 1.65, 255, 2)
   cv.putText(combined,'Canny',(460,45), cv.FONT_HERSHEY_SIMPLEX, 1.65, 255, 2)
   combined = cv.resize(combined, (1280, 960))
   cv.imshow('Combined', combined)
   
   k=cv.waitKey(5) & 0xFF
   if k==27:
       camera.release()
       break

cv.destroyAllWindows()