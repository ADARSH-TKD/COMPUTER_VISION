import cv2
import numpy as np

a =cv2.imread("car.jpg")
re_size=cv2.resize(a,(400,200))
h1 =np.vstack((re_size,re_size,re_size))
h =np.hstack((h1,h1 ))
cv2.imshow("image",h)  
cv2.waitKey(0)
cv2.destroyAllWindow()
