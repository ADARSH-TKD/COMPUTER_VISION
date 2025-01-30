import cv2
import numpy as np

# SHAPES
# img = cv2.imread("shape.png")
# gr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gr = np.float32(gr)
# res = cv2.cornerHarris(src=gr, blockSize=2, ksize=3, k=0.04, dst=None, borderType=None)
# res = cv2.dilate(res,None)

# img[res>0.01*res.max()]=[0,0,255]

# PERSON
img =cv2.imread("person.jpg")

gr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gr = np.float32(gr)
res = cv2.cornerHarris(src=gr, blockSize=2, ksize=3, k=0.04, dst=None, borderType=None)
res = cv2.dilate(res,None)

img[res>0.01*res.max()]=[0,0,255]

cv2.imshow("imagr",img)
cv2.waitKey(0)
cv2.destroyAllWindows()