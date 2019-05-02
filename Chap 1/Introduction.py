# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 22:48:40 2018

@author: MSI
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('Lenna.jpg',cv2.IMREAD_GRAYSCALE)


##cv2.imshow('image',img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
'''
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,300],[80,100],'r',linewidth=5)
plt.show()
'''

cv2.imwrite('lenna_gs.jpg',img)
