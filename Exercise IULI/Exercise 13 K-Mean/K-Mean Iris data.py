import numpy as np
import cv2
from matplotlib import pyplot as plt

X = np.random.randint(25,50,(25,2))
Y = np.random.randint(60,85,(25,2))
Z = np.vstack((X,Y))

# convert to np.float32
Z = np.float32(Z)

# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center=cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center2=cv2.kmeans(Z,3,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center3=cv2.kmeans(Z,4,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now separate the data, Note the flatten()
A1 = Z[label.ravel()==0]
B1 = Z[label.ravel()==1]

A2 = Z[label.ravel()==0]
B2 = Z[label.ravel()==1]
C2 = Z[label.ravel()==2]

A3 = Z[label.ravel()==0]
B3 = Z[label.ravel()==1]
C3 = Z[label.ravel()==2]
D3 = Z[label.ravel()==3]


# Plot the data
plt.scatter(A1[:,0],A1[:,1], c = 'r')
plt.scatter(B1[:,0],B1[:,1],c = 'g')
plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()

plt.scatter(A2[:,0],A2[:,1], c = 'r')
plt.scatter(B2[:,0],B2[:,1],c = 'g')
plt.scatter(C2[:,0],C2[:,1],c = 'b')
plt.scatter(center2[:,0],center2[:,1],s = 80,c = 'y', marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()

plt.scatter(A3[:,0],A3[:,1], c = 'r')
plt.scatter(B3[:,0],B3[:,1],c = 'g')
plt.scatter(C3[:,0],C3[:,1],c = 'b')
plt.scatter(D3[:,0],D3[:,1],c = 'm')

plt.scatter(center3[:,0],center3[:,1],s = 80,c = 'y', marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()