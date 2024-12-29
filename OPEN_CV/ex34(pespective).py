import cv2
import numpy as np
img = cv2.resize(cv2.imread("paper.png"),(300,400))

s = np.float32([[97,13],[411,122],[79,474],[430,478]])
d = np.float32([[0,0],[300,0],[0,400],[300,400]])

m=cv2.getPerspectiveTransform(s,d)
new=cv2.warpPerspective(src=img, M=m, dsize=(300,400))



cv2.imshow("image",img)
cv2.imshow("new",new)
cv2.waitKey(0)
cv2.destroyAllWindows()