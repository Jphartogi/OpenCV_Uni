# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:13:04 2018

@author: MSI
"""
import cv2 
import numpy as np

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# use sample from experiments
#green
low_green = np.uint8([[[60,105,91 ]]])
high_green = np.uint8([[[96,153,138 ]]])
hsv_green_low = cv2.cvtColor(low_green,cv2.COLOR_BGR2HSV)
hsv_green_high = cv2.cvtColor(high_green,cv2.COLOR_BGR2HSV)

#red
high_red = np.uint8([[[29,34,196]]])
low_red = np.uint8([[[17,23,130 ]]])
hsv_red_high = cv2.cvtColor(high_red,cv2.COLOR_BGR2HSV)
hsv_red_low = cv2.cvtColor(low_red,cv2.COLOR_BGR2HSV)

#blue
low_blue = np.uint8([[[185,125,32]]])
high_blue = np.uint8([[[230,190,89 ]]])
hsv_blue_high = cv2.cvtColor(high_blue,cv2.COLOR_BGR2HSV)
hsv_blue_low = cv2.cvtColor(low_blue,cv2.COLOR_BGR2HSV)

print (hsv_green_low)
print (hsv_green_high)
print (hsv_blue_low)
print (hsv_blue_high)
print (hsv_red_low)
print (hsv_red_high)

#sample

 
while (True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue= np.array([ 90 ,156, 185])
    upper_blue = np.array([110,225,230])
    
    lower_red = np.array([0,200,120])
    upper_red= np.array([5,225,200])
    
    lower_green = np.array([30,80,100])
    upper_green = np.array([45,110,160])
    mask1 = cv2.inRange(hsv,lower_blue, upper_blue)
     
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    
    mask3 = cv2.inRange(hsv,lower_green,upper_green)
    mask  = mask1 + mask2 + mask3
    res = cv2.bitwise_and(frame,frame, mask = mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('mask2',mask2)
    cv2.imshow('mask3',mask3)
    
    cv2.imshow('res',res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()    
cv2.destroyAllWindows()



