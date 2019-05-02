# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:00:26 2018

@author: MSI
"""

import cv2
import numpy as np
#
img = cv2.imread('roof.jpg')
smooth1= cv2.GaussianBlur(img,(9,9),1)
smooth2= cv2.GaussianBlur(img,(9,9),4)
smooth3= cv2.GaussianBlur(img,(9,9),6)
hori1 = np.hstack((img,smooth1,smooth2,smooth3))

cv2.imshow('parameter1&2 = 9, parameter 3 = 1,4,6',hori1)
cv2.imwrite('a.jpg',hori1)
'''
cv2.imshow('smooth1',smooth1)
cv2.imshow('smooth2',smooth2)
cv2.imshow('smooth3',smooth3)
'''

#b

smooth4 = cv2.GaussianBlur(img,(0,0),1)
smooth5 = cv2.GaussianBlur(img,(0,0),4)
smooth6 = cv2.GaussianBlur(img,(0,0),6)
hori2 = np.hstack((img,smooth4,smooth5,smooth6))

cv2.imshow('parameter1&2 = 0, parameter 3 = 1,4,6',hori2)
cv2.imwrite('b.jpg',hori2)
'''
part b are more blurry, while the K size is very low, which is 0.
'''
#c
smooth7 = cv2.GaussianBlur(img,(0,0),1,9)
cv2.imshow('nomorc',smooth7)
cv2.imwrite('c.jpg',smooth7)

#d
smooth8 = cv2.GaussianBlur(img, (0,0), 9, 1)
cv2.imshow('nomord',smooth8)
cv2.imwrite('d.jpg',smooth8)

#e.
smooth9a= cv2.GaussianBlur(smooth7, (0,0), 1, 9)
smooth9b = cv2.GaussianBlur(smooth7, (0,0), 9, 1)
cv2.imshow('nomore',smooth9a)
cv2.imshow('nomoreb',smooth9b)
cv2.imwrite('e(a).jpg',smooth9a)
cv2.imwrite('e(b).jpg',smooth9b)

#f.
smooth10 = cv2.GaussianBlur(img, (9,9), 9, 9)
smooth11 = cv2.GaussianBlur(img, (9,9), 0, 0)
cv2.imshow('nomorf',smooth10)
cv2.imshow('nomorf2',smooth11)
cv2.imwrite('f.jpg',smooth10)
cv2.imwrite('f(2).jpg',smooth11)

'''
results are not the same, because the sigma are different, while sigma x is 
very influential in bluring the image.
'''

cv2.waitKey(0)
cv2.destroyAllWindows()
