import cv2
import numpy as np

#2c
img = cv2.imread('img1.jpeg')
blur_1 = cv2.GaussianBlur(img,(0,0),1,9)
cv2.imshow('param3=1, param4=9', blur_1)
cv2.imwrite('2c_param3=1_param4=9.jpg', blur_1)
#2d
blur_2 = cv2.GaussianBlur(img,(0,0),9,1)
cv2.imshow('param3=9, param4=1', blur_2)
cv2.imwrite('2d_param3=9_param4=1.jpg', blur_2)

cv2.waitKey(0)
cv2.destroyAllWindows()