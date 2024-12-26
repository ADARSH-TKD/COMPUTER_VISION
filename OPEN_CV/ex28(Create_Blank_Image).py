import cv2
import numpy as np 
white= np.ones((400,400,3),np.uint8)*255
black= np.zeros((400,400,3),np.uint8)*255
h=np.hstack([white,black])

cv2.imshow("blank_image",h)
cv2.waitKey(0)
cv2.destroyAllWindows()