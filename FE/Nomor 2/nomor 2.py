# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 12:45:12 2018

@author: MSI
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:28:12 2018

@author: MSI
"""

import numpy as np
import cv2

hand_cascade = cv2.CascadeClassifier('hand.xml')


cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hand = hand_cascade.detectMultiScale(gray, 2, 5)
    
    for (x,y,w,h) in hand:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()