import cv2
import numpy as np,sys
from matplotlib import pyplot as plt

A = cv2.imread('scene.jpg')
titles = ['level_1','level_2','level_3','level_4','level_5','level_6']
# generate Gaussian pyramid  
G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)
for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(gpA[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# generate Laplacian pyramid
lpA = [gpA[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)
for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(lpA[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.imshow('Gaussian_pyramid1.jpg',gpA[1])
cv2.imshow('Gaussian_pyramid2.jpg',gpA[2])
cv2.imshow('Gaussian_pyramid3.jpg',gpA[3])
cv2.imshow('Gaussian_pyramid4.jpg',gpA[4])
cv2.imshow('Gaussian_pyramid5.jpg',gpA[5])
cv2.imshow('Gaussian_pyramid6.jpg',gpA[6])
cv2.imshow('laplacian_pyramid1.jpg',lpA[0])
cv2.imshow('laplacian_pyramid2.jpg',lpA[1])
cv2.imshow('laplacian_pyramid3.jpg',lpA[2])
cv2.imshow('laplacian_pyramid4.jpg',lpA[3])
cv2.imshow('laplacian_pyramid5.jpg',lpA[4])
cv2.imshow('laplacian_pyramid6.jpg',lpA[5])

cv2.waitKey(0)
cv2.destroyAllWindows()




