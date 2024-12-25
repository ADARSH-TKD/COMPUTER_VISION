import cv2
import numpy as np 
img1=cv2.resize(cv2.imread("op1.png"),(200,200))
img2=cv2.resize(cv2.imread("op2.png"),(200,200))

#addWeighted
add=cv2.addWeighted(src1=img1, alpha=1, src2=img2, beta=1, gamma=1, dst=None, dtype=None) 

#bitwise operations
#bitwise_and
new=cv2.bitwise_and(img1,img2)
#bitwise_or
new2=cv2.bitwise_or(img1,img2)

# bitwise_xor
new3=cv2.bitwise_xor(img1,img2)
#  bitwise_not
new4=cv2.bitwise_not(img1)


h1=np.hstack((new,new2))
h2=np.hstack((new3,new4))
h=np.vstack((h1,h2))
cv2.imshow("image",h)
cv2.waitKey(0)
cv2.destroyAllWindows()
