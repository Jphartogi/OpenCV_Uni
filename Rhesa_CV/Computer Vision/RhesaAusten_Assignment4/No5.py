import cv2
import numpy as np

bg = cv2.imread('Background.jpg')
fg = cv2.imread('Foreground.jpg')
bg_resize = cv2.resize(bg, (512,512))
fg_resize = cv2.resize(fg, (512,512))

bg_gray = cv2.cvtColor(bg_resize, cv2.COLOR_BGR2GRAY)
fg_gray = cv2.cvtColor(fg_resize, cv2.COLOR_BGR2GRAY)

def diff(img,img1): # returns just the difference of the two images
  return cv2.absdiff(img,img1)

def diff_remove_bg(img0,img,img1): # removes the background but requires three images 
  d1 = diff(img0,img)
  d2 = diff(img,img1)
  return cv2.bitwise_and(d1,d2)

absimg = diff(bg_gray, fg_gray)
cv2.imshow('Absolute Difference', absimg)

_, bin_thres = cv2.threshold(absimg, 20, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Thresholding', bin_thres)

kernel = np.ones((2,2),np.uint8)
opening = cv2.morphologyEx(bin_thres, cv2.MORPH_OPEN, kernel)
cv2.imshow('CV_MOP_OPEN', opening)

cv2.waitKey(0)
cv2.destroyAllWindows()