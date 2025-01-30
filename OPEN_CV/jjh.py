import cv2
img=cv2.resize(cv2.imread("leaf.jpg",0),(400,400))
cv2.imshow("leaf",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)