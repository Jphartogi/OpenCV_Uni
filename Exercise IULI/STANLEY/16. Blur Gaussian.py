# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:06:13 2018

@author: Hexidaz
"""

import cv2

img = cv2.imread('D:\Document\Spyder Project\Images\Interesting Textures.jpg')

blur3 = cv2.GaussianBlur(img,(3,3),0)
blur5 = cv2.GaussianBlur(img,(5,5),0)
blur9 = cv2.GaussianBlur(img,(9,9),0)
blur11 = cv2.GaussianBlur(img,(11,11),0)
blur5_2 = cv2.GaussianBlur(blur5,(5,5),0)

cv2.imshow('img', img)
cv2.imshow('blur3', blur3)
cv2.imshow('blur5', blur5)
cv2.imshow('blur11', blur11)
cv2.imshow('blur5_2', blur5_2)

print 'No, they dont look nearly the same since blur 5x5 is not as strong as 11x11 and by blurring it 2 times with the same strength almost does no effect except if the strength is high'

cv2.waitKey(0)
cv2.destroyAllWindows()

