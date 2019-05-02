import cv2
import numpy as np

src1 = cv2.imread("img2.jpg")
src2 = cv2.imread("img3.jpg")
src3 = cv2.imread("img1.jpeg")
src1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
src2 = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)

#a
diff12 = src1 - src2
#Because when we take the second picture there is a little movement and there is also noise
#That is why the result of substraction between src1 and src2 is not black
#but if the picture is same the result will be black(prove below)
diff12_prove = src3 - src3
#the result is black

#b
kernel = np.ones((6,6),np.uint8)
opening = cv2.morphologyEx(diff12, cv2.MORPH_OPEN, kernel)
#c
closing = cv2.morphologyEx(diff12, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Source1',src1)
cv2.imshow('Source2',src2)
cv2.imshow('src1 - src2', diff12)
cv2.imshow('substraction the same image', diff12_prove)
cv2.imshow('cleanDiff', opening)
cv2.imshow('dirtyDiff', closing)
cv2.imwrite('Source1.jpg',src1)
cv2.imwrite('Source2.jpg',src2)
cv2.imwrite('src1 - src2.jpg', diff12)
cv2.imwrite('substraction the same image.jpg', diff12_prove)
cv2.imwrite('cleanDiff.jpg', opening)
cv2.imwrite('dirtyDiff.jpg', closing)
cv2.waitKey(0)
cv2.destroyAllWindows(0)

#d
#When cleandiff is the implementation of function opening which do erode action
#and then do dilation action. That is why the result of the cleandiff have black background

#When dirtydiff is the implementation of function closing which do dilate action
#and then do erode action. That is why the result of the dirtydiff have white blackground
