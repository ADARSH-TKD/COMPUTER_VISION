import cv2
import numpy as np 

img=cv2.resize(cv2.imread("text.png"),(620,480))
new=cv2.Canny(img,100,200)
cv2.imshow("Canny",new)
cv2.waitKey(0)
cv2.destroyAllWindows()