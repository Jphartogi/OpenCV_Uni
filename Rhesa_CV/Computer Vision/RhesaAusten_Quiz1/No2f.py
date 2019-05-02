import cv2
import numpy as np

#2f
img = cv2.imread('img1.jpeg')
blur_1 = cv2.GaussianBlur(img,(1,1),0,0)
cv2.imshow('param3=0, param4=0', blur_1)
cv2.imwrite('2f_param3=0_param4=0.jpg', blur_1)
blur_2 = cv2.GaussianBlur(img,(1,1),9,9)
cv2.imshow('2f_param3=9_param4=9', blur_2)
cv2.imwrite('2f_param3=9_param4=9.jpg', blur_2)
#Yes the result is the same
#it will depends on the ksize which is diameter that is used during filtering.
#if the ksize is zero and the param3 and param4 is zero the program will error because
#there is no parameter that used for filtering
#if there is ksize, the parameter of filtering will follow the ksize which is param1 and param2

cv2.waitKey(0)
cv2.destroyAllWindows()