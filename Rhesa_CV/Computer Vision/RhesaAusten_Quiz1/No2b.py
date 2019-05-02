import cv2
import numpy as np

img = cv2.imread('img1.jpeg')
blur_1 = cv2.GaussianBlur(img,(0,0),1)
cv2.imshow('param3=1', blur_1)
cv2.imwrite('2b_param3=1.jpg', blur_1)
blur_2 = cv2.GaussianBlur(img,(0,0),4)
cv2.imshow('param3=4', blur_2)
cv2.imwrite('2b_param3=4.jpg', blur_2)
blur_3 = cv2.GaussianBlur(img,(0,0),6)
cv2.imshow('param3=6', blur_3)
cv2.imwrite('2b_param3=6.jpg', blur_3)
#Yes among the images is different
#because the the parameter 3 is sigmaColor
#Sigma color is Filter sigma in the color space.
#A larger value of the parameter means that farther colors within the pixel neighborhood will be mixed together,
#resulting in larger areas of semi-equal color.

cv2.waitKey(0)
cv2.destroyAllWindows()