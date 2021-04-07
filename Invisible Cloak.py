import numpy as np
import cv2
import time

click=cv2.VideoCapture(0)

time.sleep(3) 
for i in range(30):
    retval,back=click.read()
background=np.flip(back,axis=1)
click=cv2.VideoCapture(0)  

while (click.isOpened()):  
    ret,pic=click.read()
    if ret:
        pic=np.flip(pic,axis=1)
        
        
        ColourHSV=cv2.cvtColor(pic,cv2.COLOR_BGR2HSV)
        
        
        redStart = np.array([0,120,70])
        redEnd = np.array([10,255,255])
        redMask1 = cv2.inRange(ColourHSV,redStart,redEnd)
        
        redStart = np.array([170,120,70])
        redEnd = np.array([180,255,255])
        redMask2 = cv2.inRange(ColourHSV,redStart,redEnd)
        redMask1+=redMask2
        

        invisible = cv2.morphologyEx(redMask1, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
        #invisible = cv2.morphologyEx(redMask1, cv2.MORPH_DILATE, np.ones((5,5),np.uint8))
        pic[np.where(invisible==255)]=background[np.where(invisible==255)]
        
        
        cv2.imshow("Invisible Cloak",pic)
    key = cv2.waitKey(1)
    if key==27:
        break
click.release()
cv2.destroyAllWindows()