import cv2
import numpy as np

cap = cv2.VideoCapture("Ball Bouncing_2.mp4")
# CREATING THE REGION OF INTREST
ret, F = cap.read()
x,y,w,h = 15,36,200,440
t=(x,y,w,h)
roi = F[y:y+h,x:x+w]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi,np.array((0.,60.,32.,)),np.array((180.,255.,255.,)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
cv2.imshow("test",roi)

while True:
    ret,frame = cap.read()
    if ret == True :
        cv2.imshow("original",frame)

        if cv2.waitKey(25) & 0xFF == ord(' '):
            
            break
        
    else:
        break
cap.release()



cv2.destroyAllWindows()

