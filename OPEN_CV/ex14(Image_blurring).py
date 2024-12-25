import cv2
import numpy as np 
img=cv2.resize(cv2.imread("potrate.jpg"),(300,340))
# Apply Gaussian blur
g=cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0, dst=None, sigmaY=None, borderType=None)
# Apply Median blur
m=cv2.medianBlur(src=img,ksize=5)
# Apply Bilateral filter
b=cv2.bilateralFilter(src=img,d=9,sigmaColor=75,sigmaSpace=75)


h=np.hstack([img,g,m,b])
cv2.imshow("image",h)
cv2.waitKey(0)
cv2.destroyAllWindows()