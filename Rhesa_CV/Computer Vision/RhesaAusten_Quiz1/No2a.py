import cv2
import numpy as np

img = cv2.imread('img1.jpeg')
blur_1 = cv2.GaussianBlur(img,(9,9),1)
cv2.imshow('img1', blur_1)
cv2.imwrite('2a_param3=1.jpg', blur_1)
blur_2 = cv2.GaussianBlur(img,(9,9),4)
cv2.imshow('img2', blur_2)
cv2.imwrite('2a_param3=2.jpg', blur_2)
blur_3 = cv2.GaussianBlur(img,(9,9),6)
cv2.imshow('img3', blur_3)
cv2.imwrite('2a_param3=6.jpg', blur_3)

cv2.waitKey(0)
cv2.destroyAllWindows()