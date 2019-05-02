import cv2 as cv
import numpy as np


img = cv.imread('img_3.jpg')
font = cv.FONT_HERSHEY_SIMPLEX

#cv.Not(im,im)
#f=cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX,1.0,1.0,1.0,1,8)
cv.namedWindow("Display")

#	this is the method to define a mouse callback function. Several events are given in OpenCV documentation
def my_mouse_callback(event,x,y,flags,param):
	if event==cv.EVENT_LBUTTONDBLCLK:		# here event is left mouse button double-clicked
		px = img[x,y]
		print px
		
		#text="{0},{1}".format(x,y)
		#cv.PutText(im,text,(x+5,y+5),f,cv.RGB(0,255,255))

cv.setMouseCallback("Display",my_mouse_callback)	#binds the screen,function and image

while(1):
	cv.imshow("Display",img)
	if cv.waitKey(15)%0x100==27:
		break		# waiting for clicking escape key
cv.destroyAllWindow("Display")