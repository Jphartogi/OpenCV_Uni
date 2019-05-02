# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:50:17 2018

@author: MSI
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 23:03:21 2018

@author: MSI
"""

import cv2
import numpy as np

red_lower_trial = np.uint8([[[0,1,180]]])
hsv_res_low = cv2.cvtColor(red_lower_trial,cv2.COLOR_BGR2HSV)
print hsv_res_low

red_higher_trial = np.uint8([[[80,80,220 ]]])
hsv_res_high = cv2.cvtColor(red_higher_trial,cv2.COLOR_BGR2HSV)
print hsv_res_high

img = cv2.imread('jelly.jpg')
 
rows2,cols2,channels2 = img.shape

'''
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
px = hsv[110,35]
print px
''' 
lower_red = np.array([0,180,175])
upper_red = np.array([10,255,230])

    
mask = cv2.inRange(hsv,lower_red, upper_red)
res = cv2.bitwise_and(img,img, mask = mask) ##bitwise-> where there is something in the frame and mask is true
'''                                                    ## mask is in range of lower red, upper red. if in the range = true.
cv2.imshow('hsv',hsv)

cv2.imshow('mask',mask)
'''
cv2.imshow('res',res)
cv2.imshow('frame',img)
    
   
cv2.waitKey(0)    
cv2.destroyAllWindows()