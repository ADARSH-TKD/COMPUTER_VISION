import cv2
import numpy as np 
img=cv2.imread("sudoko.jpg")
g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
c=cv2.Canny(g,20,256)

lines = cv2.HoughLinesP(image = c, rho=1, theta=np.pi/180, threshold=200, lines=None, minLineLength=180, maxLineGap=100)


for i in lines:
    x1,y1,x2,y2 = i[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    
    
print(lines)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()