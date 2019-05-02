import cv2
import numpy as np

img = cv2.imread("texture.jpeg")
blur_1 = cv2.GaussianBlur(img,(3,3),0)
cv2.imshow('img1', blur_1)
blur_2 = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('img2', blur_2)
blur_3 = cv2.GaussianBlur(img,(9,9),0)
cv2.imshow('img3', blur_3)
blur_4 = cv2.GaussianBlur(img,(11,11),0)
cv2.imshow('img4', blur_4)

#4b
#The picture will become more blur when the standard deviation of X and Y bigger
#The standard deviation of X and Y will affect the blur of the image, this is how gaussian blur remove high frequency (noise)
#beside that amount of sigmaX and sigmaY depends on the size of the image.



cv2.waitKey(0)
cv.destroyAllWindows()