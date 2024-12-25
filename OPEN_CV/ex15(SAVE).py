import cv2
img=cv2.imread("car.jpg",0)

cv2.imwrite(filename="bcar.jpg", img=img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()