import cv2
import numpy as np 

def color(x):
    pass
img =np.zeros((500,500,3),np.int8)
# print(img)
cv2.namedWindow("color")
cv2.createTrackbar("bar","color",10,110,color)
while True:
    cv2.imshow("color",img)
    if cv2.waitKey(1) & 0xff==ord("p"):
        break
    p=cv2.getTrackbarPos("bar","color")
    print(p)
    img[:]=[p,0,0]

cv2.destroyAllWindows()