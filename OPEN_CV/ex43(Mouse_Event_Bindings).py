import cv2
import numpy as np
import matplotlib.pyplot as plt
#python function
def python(event,x,y,flag,p):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5 ,(0,0,255),-1)
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,255,0),-1)
    
# Create images with pixel values in the valid range
img = np.ones((400, 400, 3), dtype=np.uint8) * 255  # White image
cv2.namedWindow("adarsh")
cv2.setMouseCallback("adarsh",python)
while True:
    cv2.imshow("adarsh",img)
    if cv2.waitKey(25) & 0xff== ord("p"):
        break
    
    
cv2.destroyAllWindows()
