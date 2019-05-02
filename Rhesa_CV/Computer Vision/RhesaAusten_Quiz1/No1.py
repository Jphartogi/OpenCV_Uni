import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    ret, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([136,87,111])
    upper_red = np.array([180,255,255])

    lower_blue = np.array([99,115,150])
    upper_blue = np.array([110,255,255])

    lower_green = np.array([50,50,100])
    upper_green = np.array([100,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = mask + mask1 + mask2

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    res1 = cv2.bitwise_and(frame,frame, mask=mask1)
    res2 = cv2.bitwise_and(frame,frame, mask=mask2)
    result = cv2.bitwise_and(frame,frame, mask=mask3)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('res1',res1)
    cv2.imshow('res2',res2)
    cv2.imshow('result', result)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()