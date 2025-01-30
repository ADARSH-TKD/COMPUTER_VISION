import cv2
import numpy as np

a =cv2.imread("car.jpg")
re_size=cv2.resize(a,(400,600))
cv2.imshow("image",re_size)
cv2.waitKey(0)
cv2.destroyAllWindow()