import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True) :
	ret, frame = cap.read()
	canny = cv2.Canny(frame,140,220)

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow('original',frame)
	cv2.imshow('canny',canny)
	cv2.imshow('gray', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()  