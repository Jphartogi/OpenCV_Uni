# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 12:25:45 2018

@author: MSI
"""

import cv2


img = cv2.imread('scene.jpg')
img_array = [img]
for x in xrange(0,3):
    img = cv2.pyrDown(img)
    img_array.append(img)
'''
image1 = cv2.pyrDown(img)
image2 = cv2.pyrDown(image1)
image3 = cv2.pyrDown(image2)
image4 = cv2.pyrDown(image3)
'''
cv2.imshow("pyr0", img_array[0])
cv2.imshow("pyr1", img_array[1])
cv2.imshow("pyr2", img_array[2])
cv2.imshow("pyr3", img_array[3])

cv2.waitKey(0)
cv2.destroyAllWindows()

    

