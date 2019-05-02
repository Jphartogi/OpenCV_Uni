# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:47:19 2018

@author: MSI
"""

import cv2
from Tkinter import *
import tkMessageBox


window = Tk()
window.wm_withdraw()



#centre screen message
window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
tkMessageBox.showinfo(title="How To use", message="Hello""\n""To use this program ""\n""press the left button anywhere on the image""\n"
                      "and then there will be a pop up message to give you the info of the position"
                      "\n""Thank you :) and enjoy the app")

search = False
img = cv2.imread('jelly.jpg')
height, width, color_space = img.shape

def find(event, x, y, flags, params):
     global coordinate,pixel_val,search
     if event == cv2.EVENT_LBUTTONDOWN:
         search = True
         if search == True :
             print "Coordinate"
             b, g, r = img[y,x]
             window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
             tkMessageBox.showinfo(title="Info!",message=["Coordinate: ",x,y,"  Color value(BGR):  ",b,g,r])
             print [x,y]
         
    
         
     elif event == cv2.EVENT_LBUTTONUP:
         search = False
     elif event == cv2.EVENT_RBUTTONUP:
         search = False
     elif event == cv2.EVENT_MOUSEMOVE:
         search = False

cv2.namedWindow('image')

cv2.resizeWindow('image', width, height)

cv2.setMouseCallback('image', find)


while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
