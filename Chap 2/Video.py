# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:07:01 2018

@author: MSI
"""

import cv2 


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640 , 480))  
                    ##(filename & ext, codec , fps , size)

while (True):
    ret, frame = cap.read() 
    ## ret = return true
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    out.write(frame)
    cv2.imshow('frame',frame)
    
    cv2.imshow('gray',gray)
    
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()

