# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 09:08:34 2018

@author: Hexidaz
"""

print "Press l, c, e to change brush mode to line, circle, ellipse"

import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
size = 0
b = 0
g = 0
r = 0
pts = 0
erase = False
r1 = 0
r2 = 0
radius = 0

#--------------------------------------Mouse Event--------------------------------------
def mouse_callback(event, x, y, flags, param):
    global ix, iy, drawing, mode, pts, size, b, g, r, erase, elevation, r1, r2, radius
    #--------------------------------------Eraser--------------------------------------
    if event == cv2.EVENT_RBUTTONDOWN:
        erase = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if erase == True:
            if size <= 0:
                pass
            elif size >= 1:
                cv2.rectangle(canvas, (x-size,y-size), (x+size,y+size), 0, -1)
    elif event == cv2.EVENT_RBUTTONUP:
        erase = False
    #--------------------------------------Eraser--------------------------------------
    #--------------------------------------Drawer--------------------------------------
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == "line":
            cv2.line(canvas, (ix,iy), (x,y), (b,g,r), size)
        if mode == "circle":
            r1 = abs(x-ix)
            r2 = abs(y-iy)
            if r1 > r2:
                radius = r1
            elif r2 > r1:
                radius = r2
            cv2.circle(canvas, (ix,iy), radius, (b,g,r), -1)
        if mode == "ellipse":
            cv2.ellipse(canvas,(ix,iy), (abs(x-ix),abs(y-iy)), elevation, 0, 360, (b,g,r), -1)
        if mode == "polygon":
            pts = np.append([x,y])
        if k == ord('d'):
            cv2.polylines(canvas, [pts], True, (b,g,r), size)
    #--------------------------------------Drawer--------------------------------------
#--------------------------------------Mouse Event--------------------------------------


#--------------------------------------Color Picker--------------------------------------
def nothing(x):
    pass

# Create a black image, a window
canvas = np.zeros((800,1400,3), np.uint8)
#canvas = np.full(canvas.shape, 255, np.uint8)
cv2.namedWindow('Canvas')

# create trackbars for color change
cv2.createTrackbar('Thickness', 'Canvas', 0, 100, nothing)
cv2.createTrackbar('R', 'Canvas', 0, 255, nothing)
cv2.createTrackbar('G', 'Canvas', 0, 255, nothing)
cv2.createTrackbar('B', 'Canvas', 0, 255, nothing)
cv2.createTrackbar('Elevation', 'Canvas', 0, 90, nothing)

cv2.createTrackbar('AND', 'Canvas',0,1,nothing)
cv2.createTrackbar('OR', 'Canvas',0,1,nothing)
cv2.createTrackbar('XOR', 'Canvas',0,1,nothing)

cv2.setMouseCallback('Canvas',mouse_callback)

while(1):
    cv2.imshow('Canvas', canvas)
    
    size = cv2.getTrackbarPos('Thickness', 'Canvas')
    r = cv2.getTrackbarPos('R', 'Canvas')
    g = cv2.getTrackbarPos('G', 'Canvas')
    b = cv2.getTrackbarPos('B', 'Canvas')
    elevation = cv2.getTrackbarPos('Elevation', 'Canvas')
    AND = cv2.getTrackbarPos('AND', 'Canvas')
    OR = cv2.getTrackbarPos('OR', 'Canvas')
    XOR = cv2.getTrackbarPos('XOR', 'Canvas')
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    #--------------------------------------Mode Select--------------------------------------
    if k == ord("c"):
        mode = "circle"
    if k == ord("e"):
        mode = "ellipse"
    if k == ord("l"):
        mode = "line"
    if k == ord("p"):
        mode = "polygon"
        pts = 0
#    if k == ord('d') & mode == "polygon":
#        cv2.polylines(canvas, [pts], True, (b,g,r), size)
    #--------------------------------------Mode Select--------------------------------------

    # get current positions of four trackbars
    
#--------------------------------------Color Picker--------------------------------------
cv2.destroyAllWindows()