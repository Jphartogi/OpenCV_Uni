# -*- coding: utf-8 -*-
"""
Created on Tue May 08 13:54:43 2018

@author: MSI
"""

import numpy as np
import cv2

img = cv2.imread('home.jpg')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

ret,label,center=cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

ret,label,center2=cv2.kmeans(Z,3,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center2 = np.uint8(center2)
res3 = center2[label.flatten()]
res4 = res3.reshape((img.shape))

ret,label,center3=cv2.kmeans(Z,4,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center3 = np.uint8(center3)
res5 = center3[label.flatten()]
res6 = res5.reshape((img.shape))

ret,label,center4=cv2.kmeans(Z,5,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center4 = np.uint8(center4)
res7 = center4[label.flatten()]
res8 = res7.reshape((img.shape))



numpy_horizontal = np.hstack((res2,res4))
numpy_horizontal2 = np.hstack((res6,res8))
numpy_vertical = np.vstack((numpy_horizontal,numpy_horizontal2))


cv2.imshow('result',numpy_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()