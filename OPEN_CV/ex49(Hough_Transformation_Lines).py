import cv2
import numpy as np 
import matplotlib.pyplot as plt 
 
img = cv2.imread("sudoko.jpg")#read the image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert the image to gray scale

edg =cv2.Canny(gray,50,250,apertureSize = 3)#apply canny edge detection

lines = cv2.HoughLines(image=edg, rho=1, theta=np.pi/180, threshold=200, lines=None, srn=None, stn=None, min_theta=None, max_theta=None)#apply hough transformation

for r,th in lines[0]:#loop through the lines
    a=np.cos(th)#get the cos of the angle
    b=np.sin(th)#get the sin of the angle
    
    x0 = a*r #get the x0
    y0 = b*r #get the y0
    
    x1 = int(x0 + 1000*(-b))#get the x1
    y1 = int(y0 + 1000*(a))#get the y1
    x2 = int(x0 - 1000*(-b))#get the x2
    y2 = int(y0 - 1000*(a))#get the y2
    #draw the lines
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    

print(lines)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()