import cv2
import numpy as np 

img=cv2.resize(cv2.imread("love.jpg"),(200,200))
mask=np.float32([[1,0,100],[0,1,50]])
new=cv2.warpAffine(img,mask,(0))
print(img)
print(new)
 
cv2.imshow("image",new)
cv2.waitKey(0)
cv2.destroyAllWindows()