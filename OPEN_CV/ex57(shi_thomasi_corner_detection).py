import cv2
import numpy as np

img = cv2.imread("shape.png")
g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cr = cv2.goodFeaturesToTrack(g,50,0.01,20)
cr = np.int64(cr)

for i in cr:
    x,y =i.ravel()
    cv2.circle(img,(x,y),5,(0 ,0,0))

cv2.imshow("shape",img)
cv2.waitKey(0)
cv2.destroyAllWindows()