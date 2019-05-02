import cv2
import numpy as np

img = cv2.imread("scene1.jpg")
kernel = np.ones((1024,768),np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('tophat_morphological', tophat)
ret, mask = cv2.threshold(tophat, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('mask', mask)
add = cv2.add(tophat, mask)
cv2.imshow('combine', add)


cv2.waitKey(0)
cv2.destroyAllWindows()
