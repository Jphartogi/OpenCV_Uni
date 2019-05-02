print(__doc__)
import cv2
import numpy as np
from matplotlib import pyplot as plt

from sklearn import datasets

iris = datasets.load_iris()

X = iris.data

Z = np.float32(X)

criteria = (cv2.TERM_CRITERIA_EPS +cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 3;
ret,label,center=cv2.kmeans(Z,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

criteria = (cv2.TERM_CRITERIA_EPS +cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 4;
ret,label,center1=cv2.kmeans(Z,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

criteria = (cv2.TERM_CRITERIA_EPS +cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 2;
ret,label,center2=cv2.kmeans(Z,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

A = Z[label.ravel()==0]
B = Z[label.ravel()==1]
C = Z[label.ravel()==2]
D = Z[label.ravel()==3]



plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(C[:,0],C[:,1],c = 'g')
plt.scatter(center[:,0],center[:,1], s = 75, c = 'k', marker = 's')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.show()

plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(C[:,0],C[:,1],c = 'g')
plt.scatter(D[:,0],D[:,1],c = 'b')
plt.scatter(center1[:,0],center1[:,1], s = 75, c = 'k', marker = 's')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.show()

plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(C[:,0],C[:,1],c = 'g')
plt.scatter(center2[:,0],center2[:,1], s = 75, c = 'k', marker = 's')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.show()
