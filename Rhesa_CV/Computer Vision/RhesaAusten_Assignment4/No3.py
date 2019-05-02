import cv2
import numpy as np

print "press c for circle"
print "press l for line"
print "press r for rectangel"
print "press e for ellipse"
print "press p for polygon"
print "press m for erase"
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
# mouse callback function
def simple_paint(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == 'rect':
                cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
            elif mode == 'circle':
                cv2.circle(img,(x,y),20,(b,g,r),-1)
            elif mode == 'line':
                cv2.line(img,(ix,iy),(x,y),(b,g,r),5)
            elif mode == 'ellipse':
                cv2.ellipse(img,(ix,iy),(x,y),elevation,0,360,255,-1)
            elif mode == 'polygon':
                pts = np.append([x,y])
                cv2.polylines(canvas, [pts], True, (b,g,r), size)    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == 'rect':
            cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
        elif mode == 'circle':
            cv2.circle(img,(x,y),20,(b,g,r),-1)
        elif mode == 'line':
            cv2.line(img,(ix,iy),(x,y),(b,g,r),5)
        elif mode == 'ellipse':
            cv2.ellipse(img,(ix,iy),(x,y),elevation,0,360,255,-1)
        elif mode == 'polygon':
            pts = np.append([x,y])
            cv2.polylines(img, [pts], True, (b,g,r), size) 
    if event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
       if drawing == True:
            if mode == False:
                cv2.rectangle(img,(ix,iy),(x,y),(0,0,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,0),-1)
    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,0,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,0),-1)
    

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.namedWindow('image1')
cv2.setMouseCallback('image',simple_paint)


def nothing(x):
    pass

# Create a black image, a window



cv2.createTrackbar('Thickness', 'image', 0, 100, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('Elevation', 'image', 0, 90, nothing)
# create switch for ON/OFF functionality
#switch1 = 's1'
#switch2 = 's2'
AND_switch = 'AND'
OR_switch = 'OR'
XOR_switch = 'XOR'
#cv2.createTrackbar(switch1, 'image',0,1,nothing)
#cv2.createTrackbar(switch2, 'image',0,1,nothing)
cv2.createTrackbar(AND_switch, 'image1',0,1,nothing)
cv2.createTrackbar(OR_switch, 'image1',0,1,nothing)
cv2.createTrackbar(XOR_switch, 'image1',0,1,nothing)


    

    
      
while(1):
    # get current positions of four trackbars
    thick = cv2.getTrackbarPos('Thickness', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    elevation = cv2.getTrackbarPos('Elevation', 'image')
    AND = cv2.getTrackbarPos(AND_switch,'image1')
    OR = cv2.getTrackbarPos(OR_switch,'image1')
    XOR = cv2.getTrackbarPos(XOR_switch,'image1')
    #s1 = cv2.getTrackbarPos(switch1,'image')
    #s2 = cv2.getTrackbarPos(switch2,'image')
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF

    if AND == 1:
        b > 0
        r > 0
        g > 0
    if k == ord('m'):
        mode = not mode
    if k == ord('l'):
        mode = 'line'
    if k == ord('c'):
        mode = 'circle'
    if k == ord('r'):
        mode = 'rect'
    if k == ord('p'):
        mode = 'poly'
    if k == ord('e'):
        mode == 'ellipse'
    elif k == 27:
        break

#for the polygon and ellipse still have an error

cv2.destroyAllWindows()
