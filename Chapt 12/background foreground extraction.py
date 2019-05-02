# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:23:31 2018

@author: MSI
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('joshua.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (500,500,4000,2000)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img= img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
