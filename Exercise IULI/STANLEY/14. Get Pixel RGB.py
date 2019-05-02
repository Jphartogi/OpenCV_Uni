# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 08:52:47 2018

@author: Hexidaz
"""

import cv2

img = cv2.imread('D:\Document\Spyder Project\Images\SHELTER.jpg')
height, width, color_space = img.shape

def mouse_callback(event, x, y, flags, params):
    #right-click event value is 2, 1 is left click
    if event == 1:
        #global right_clicks
        #store the coordinates of the right-click event
        #right_clicks = [x,y]
        #this just verifies that the mouse data is being collected
        #you probably want to remove this later
        #print right_clicks
        print "Coordinate"
        print [x,y]
        #must reverse the x and y because its img[row, coloumn]
        #https://stackoverflow.com/questions/48991494/program-to-identify-pixel-color-on-mouse-click-using-python-tkinter
        #https://stackoverflow.com/questions/25642532/opencv-pointx-y-represent-column-row-or-row-column/25644503#25644503
        b, g, r = img[y,x]
        print "Color Value"
        print r, g, b
        print

#Create area to detect mouse ?
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#resize the area to detect mouse
cv2.resizeWindow('image', width, height)
#calling mouse fundtion
cv2.setMouseCallback('image', mouse_callback)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
