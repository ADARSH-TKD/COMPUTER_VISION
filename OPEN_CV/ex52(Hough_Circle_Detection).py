import cv2
import numpy as np 

img=cv2.resize(cv2.imread("BALL.jpg"),(700,500))#read the image
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert the image to gray scale
c=cv2.Canny(gry,20,256)#apply canny edge detection


circles=cv2.HoughCircles(image=c, method=cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=100, param2=39, minRadius=0, maxRadius=0)#apply hough transformation
data=np.int16(np.around(circles))
for (x,y,r) in data[0,:]:
    cv2.circle(img,(x,y),r,(0,255,0),2)
    # cv2.ellipse(img=img, center=(x, y), axes=(50, 70), angle=-2, startAngle=10, endAngle=360, color=(0, 255, 0), thickness=1, lineType=16, shift=0)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()