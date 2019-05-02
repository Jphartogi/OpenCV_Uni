import cv2
import numpy as np
import ctypes  # An included library with Python install.
from Tkinter import *
import tkMessageBox


window = Tk()
window.wm_withdraw()



#centre screen message
window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
tkMessageBox.showinfo(title="How To use", message="Hello""\n""To use this program please select one of the given mode:""\n" 
         "press e for ellipse""\n""press c for circle""\n""press l for line""\n""to start drawing press the left click""\n"
         "to erase press the right click""\n""to quit press esc""\n""Thank you :) and enjoy the app")

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1


# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,eraser,r1,r2,radius,b,g,r

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if AND == 1:
            b, g, r = img[y,x]
            if b > 0 and g > 0 and r > 0:
                if drawing == True :
                    if mode == "circle" :
                        r1 = abs(x-ix)
                        r2 = abs(y-iy)
                        if r1 > r2:
                            radius = r1
                        elif r2 > r1:
                            radius = r2
                        cv2.circle(img, (ix,iy), radius, (255,255,255), -1)
                    if mode == "line" :
                        cv2.circle(img,(x,y),2,(255,255,0),10)
                    if mode == "ellipse":
                        cv2.ellipse(img,(ix,iy), (abs(x-ix),abs(y-iy)), 5, 0, 360, (255,0,255), -1)
                elif drawing == False:
                    if eraser == True:
                        cv2.circle(img,(x,y),100,(0,0,0),-1)
        elif OR == 1:
            b, g, r = img[y,x]
            if b > 0 or g > 0 or r > 0:
                if drawing == True :
                    if mode == "circle" :
                        r1 = abs(x-ix)
                        r2 = abs(y-iy)
                        if r1 > r2:
                            radius = r1
                        elif r2 > r1:
                            radius = r2
                        cv2.circle(img, (ix,iy), radius, (255,255,255), -1)
                    if mode == "line" :
                        cv2.circle(img,(x,y),2,(255,255,0),10)
                    if mode == "ellipse":
                        cv2.ellipse(img,(ix,iy), (abs(x-ix),abs(y-iy)), 5, 0, 360, (255,0,255), -1)
                elif drawing == False:
                    if eraser == True:
                        cv2.circle(img,(x,y),100,(0,0,0),-1)
        else :
             if drawing == True :
                 if mode == "circle" :
                     r1 = abs(x-ix)
                     r2 = abs(y-iy)
                     if r1 > r2:
                         radius = r1
                     elif r2 > r1:
                         radius = r2
                     cv2.circle(img, (ix,iy), radius, (255,255,255), -1)
                 if mode == "line" :
                     cv2.circle(img,(x,y),2,(255,255,0),10)
                 if mode == "ellipse":
                     cv2.ellipse(img,(ix,iy), (abs(x-ix),abs(y-iy)), 5, 0, 360, (255,0,255), -1)
             elif drawing == False:
                 if eraser == True:
                        cv2.circle(img,(x,y),100,(0,0,0),-1)
                
    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        eraser = False
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        drawing = False
        eraser = True
       
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    
def nothing(x):
    pass   

img = np.zeros((1024,1024,3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('AND', 'image',0,1,nothing)
cv2.createTrackbar('OR', 'image',0,1,nothing)
cv2.createTrackbar('XOR', 'image',0,1,nothing)
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    AND = cv2.getTrackbarPos('AND', 'image')
    OR = cv2.getTrackbarPos('OR','image')
    XOR = cv2.getTrackbarPos('XOR', 'image')
    k = cv2.waitKey(1) & 0xFF
    if k == ord('c'):
        mode = "circle"
    if k == ord('l'):
        mode = "line"
    if k == ord('e'):
        mode = "ellipse"
    elif k == 27:
        break

cv2.destroyAllWindows()