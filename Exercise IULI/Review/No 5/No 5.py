# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 12:45:31 2018

@author: MSI
"""
import cv2
import numpy as np
Mug = cv2.imread('WithMug.jpg')
Gray_Mug = cv2.cvtColor(Mug,cv2.COLOR_BGR2GRAY)
NoMug = cv2.imread('NoMug.jpg')
Gray_NoMug = cv2.cvtColor(NoMug,cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.uint8)
Diff = cv2.absdiff(Gray_Mug,Gray_NoMug)

cv2.imshow('With Mug',Mug)
cv2.imshow('No Mug' ,NoMug)
cv2.imshow("Abs_value ",Diff)



	#b
retval,thresh = cv2.threshold(Diff,50,255,cv2.THRESH_BINARY)
cv2.imshow("binary threshold ",thresh)
      

	#c
newimage = cv2.morphologyEx(Diff,cv2.MORPH_OPEN,kernel)

cv2.imshow("MORPH_OPEN",newimage);
'''
	#d
cv2.erode(temp,temp,Mat());
matMug.copyTo(temp2,temp);
imshow("an outline of the coffee cup",temp2);
'''
cv2.waitKey(0)
cv2.destroyAllWindows()
