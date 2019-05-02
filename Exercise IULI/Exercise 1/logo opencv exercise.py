# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:08:58 2018

@author: Jphartogi
"""
import numpy as np
import cv2  #3.0.0-dev 
import math

r1 = 70
r2 = 30

ang = 60

d = 170
h = int(d/2*math.sqrt(3))

dot_red = (256,128)
dot_green = (dot_red[0]-85, dot_red[1]+h)
dot_blue = (dot_red[0]+85, dot_red[1]+h)

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

# tan = float(dot_red[0]-dot_green[0])/(dot_green[1]-dot_red[0])
# ang = math.atan(tan)/math.pi*180

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
black = (255,255,255)

full = -1

img = np.zeros((512, 512, 3), np.uint8)
img[:] = [255,255,255]
cv2.circle(img, dot_red, r1, red, full)
cv2.circle(img, dot_green, r1, green, full)
cv2.circle(img, dot_blue, r1, blue, full)
cv2.circle(img, dot_red, r2, black, full)
cv2.circle(img, dot_green, r2, black, full)
cv2.circle(img, dot_blue, r2, black, full)

cv2.ellipse(img, dot_red, (r1, r1), ang, 0, ang, black, full)
cv2.ellipse(img, dot_green, (r1, r1), 360-ang, 0, ang, black, full)
cv2.ellipse(img, dot_blue, (r1, r1), 360-2*ang, ang, 0, black, full)
cv2.putText(img,"Open CV",(130,450),font,2,(0,0,0),5)



cv2.imwrite("opencv_logo.png", img)



