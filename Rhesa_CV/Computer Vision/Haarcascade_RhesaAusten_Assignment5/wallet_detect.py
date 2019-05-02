import numpy as np
import cv2



wallet_cascade = cv2.CascadeClassifier('walletdetector.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    wallet = wallet_cascade.detectMultiScale(gray, 2, 5)

   

    for (i,(x,y,w,h)) in enumerate(wallet):
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #cv2.putText(img, "Wallet #{}".format(i + 1), (x, y - 10),
        #cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
 
       
 

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()