import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('scene.jpg',0)
ret,thresh1 = cv.threshold(img,128,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,128,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,128,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,128,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,128,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

img = cv.medianBlur(img,5)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,15,5)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,15,5)
cv.imshow('param1 = 5, ADAPTIVE_THRESH_MEAN_C', th2)
cv.imshow('param1 = 5, ADAPTIVE_THRESH_GAUSSIAN_C', th3)

img = cv.medianBlur(img,5)
th4 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,9,0)
th5 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,9,0)
cv.imshow('param1 = 0, ADAPTIVE_THRESH_MEAN_C', th4)
cv.imshow('param1 = 0, ADAPTIVE_THRESH_GAUSSIAN_C', th5)

img = cv.medianBlur(img,5)
th6 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,13,-5)
th7 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,13,-5)
cv.imshow('param1 = -5, ADAPTIVE_THRESH_MEAN_C', th6)
cv.imshow('param1 = -5, ADAPTIVE_THRESH_GAUSSIAN_C', th7)

cv.waitKey(0)
cv.destroyAllWindows()
