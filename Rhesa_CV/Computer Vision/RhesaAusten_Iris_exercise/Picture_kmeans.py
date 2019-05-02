import numpy as np
import cv2

img = cv2.imread('home.jpg')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center1=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)



# Now convert back into uint8, and make original image
center = np.uint8(center)
res1 = center[label.flatten()]
res_K3 = res1.reshape((img.shape))

center1 = np.uint8(center1)
res2 = center1[label.flatten()]
res_K2 = res2.reshape((img.shape))





#cv2.imwrite('K=4', res_K4)
#cv2.imwrite('K=2.jpg', res_K2)
cv2.imwrite('K=3.jpg', res_K3)
cv2.waitKey(0)
cv2.destroyAllWindows()
