# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:07:49 2018

@author: MSI
"""

import cv2
import numpy as np

img = cv2.imread('scene.jpg')
ret,val1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
ret,val2 = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)
ret,val3 = cv2.threshold(img,128,255,cv2.THRESH_TRUNC)
ret,val4 = cv2.threshold(img,128,255,cv2.THRESH_TOZERO)
ret,val5 = cv2.threshold(img,128,255,cv2.THRESH_TOZERO_INV)

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
numpy_horizontal = np.hstack((img,val1,val2))
numpy_horizontal2 = np.hstack((val3,val4,val5))
vertical = np.vstack((numpy_horizontal,numpy_horizontal2))

l1, w1, d1 = vertical.shape
black = np.zeros((l1/7, w1, d1), np.uint8)
hcat = cv2.vconcat((black, vertical))
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(hcat,'The order from left to right Ori,Binary,Binary_inv,Trunc,ToZero,ToZero_inv',(40,50), font, 0.8,(255, 255, 255), 3, 0)


adp_val1 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,5)
adp_val2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,9,5)
adp_val3 =  cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,5)
adp_val4 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,5)
hori1 = np.hstack((adp_val1,adp_val2,adp_val3,adp_val4))
l2, w2= hori1.shape
black2 = np.zeros((l2/7, w2), np.uint8)
hcat2 = cv2.vconcat((black2, hori1))
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(hcat2,'Adaptive threshold param 5, The order Mean-Binary, Mean-Binary_INV, Gaus-Binary,Gaus-Binary_inv',(10,20), font, 0.8,(255, 255, 255), 3, 0)


adp_val5 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,0)
adp_val6 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,9,0)
adp_val7 =  cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,0)
adp_val8 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,0)
hori2 = np.hstack((adp_val5,adp_val6,adp_val7,adp_val8))
l3, w3= hori2.shape
black3 = np.zeros((l3/7, w3), np.uint8)
hcat3 = cv2.vconcat((black3, hori2))
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(hcat3,'Adaptive threshold param 0, The order Mean-Binary, Mean-Binary_INV, Gaus-Binary,Gaus-Binary_inv',(10,20), font, 0.8,(255, 255, 255), 3, 0)


adp_val9 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,-5)
adp_val10 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,9,-5)
adp_val11 =  cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,-5)
adp_val12 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,-5)
hori3 = np.hstack((adp_val9,adp_val10,adp_val11,adp_val12))
l4, w4= hori3.shape
black4 = np.zeros((l4/7, w4), np.uint8)
hcat4 = cv2.vconcat((black4, hori3))
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(hcat4,'Adaptive threshold param -5, The order Mean-Binary, Mean-Binary_INV, Gaus-Binary,Gaus-Binary_inv',(10,20), font, 0.8,(255, 255, 255), 3, 0)

cv2.imshow('task ',hcat)
cv2.imshow('task a',hcat2)
cv2.imshow('task b(1)',hcat3)
cv2.imshow('task b(2)',hcat4)
#ret val_adp1 = cv2.adaptiveThreshold()

cv2.waitKey(0)
cv2.destroyAllWindows()


