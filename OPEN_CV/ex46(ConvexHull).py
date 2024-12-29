import cv2
import numpy as np 

org=cv2.resize(cv2.imread("shape.png"),(500,500))
img=cv2.cvtColor(org,cv2.COLOR_BGR2GRAY)
_,th=cv2.threshold(img,200,255,cv2.THRESH_BINARY)
cnt,h=cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
new=cv2.drawContours(org,cnt,-1,(0,255,0),2)

for c in cnt:
    m = cv2.moments(c) 
    x= int(m["m10"]/m["m00"])
    y= int(m["m01"]/m["m00"])
    cv2.drawContours(org,cnt,-1,(0,0,0),2)
    cv2.circle(org,(x,y),5,(0,0,0),-1)
    area=cv2.contourArea(c)
    
    epsilon = 0.001*(cv2.arcLength(c,True))#0.1 is the accuracy of the approximation
    d=cv2.approxPolyDP(c,epsilon, True)
    h=cv2.convexHull(d)
    x,y,w,h=cv2.boundingRect(h)
    cv2.rectangle(img=org,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=2) 

cv2.imshow("image",new)
cv2.waitKey(0)
cv2.destroyAllWindows()