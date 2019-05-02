# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:55:13 2018

@author: MSI
"""

import cv2
import numpy as np

img = cv2.imread('Daun2.jpg')
hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('daun hsv' , hsv)
cv2.imshow('daun',img)