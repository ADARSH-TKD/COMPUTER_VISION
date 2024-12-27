import cv2
import numpy as np
def color(x):
    pas
img=np.ones((500,500,3),np.uint8)*255
cv2.namedWindow("color")

cv2.createTrackbar("R", "color", 0, 255,color)
cv2.createTrackbar("G", "color", 0, 255,color)
cv2.createTrackbar("B", "color", 0, 255,color)
while True:
    cv2.imshow("color",img)
    if cv2.waitKey(1) and 0xff==ord(" "):
        break
    r=cv2.getTrackbarPos("R","color")
    g=cv2.getTrackbarPos("G","color")
    b=cv2.getTrackbarPos("B","color")
    
    img[:]=[b,g,r]
    

cv2.destroyAllWindows()