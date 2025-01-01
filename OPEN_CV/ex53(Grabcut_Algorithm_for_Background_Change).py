import cv2
import numpy as np 

img = cv2.imread("car3.jpg")
mask1=np.zeros(img.shape[:2],np.int8)

back_mask=np.zeros((1,65),np.float64)*255

object_mask=np.zeros((1,65),np.float64)*255


#   x1,y1,x2,y2
r = [52,47,557,350]
  
cv2.grabCut(img=img, mask=mask1, rect=r, bgdModel=back_mask, fgdModel=object_mask, iterCount=10, mode=cv2.GC_INIT_WITH_RECT)

mask2=np.where((mask1 == 2)| (mask1 ==0),0,1).astype(int)

im = img*mask2[:,:,np.newaxis]
# Convert image to correct data type
im = np.clip(im, 0, 255).astype(np.uint8)

cv2.imshow("filter image",im)
cv2.waitKey(0)
cv2.destroyAllWindows() 