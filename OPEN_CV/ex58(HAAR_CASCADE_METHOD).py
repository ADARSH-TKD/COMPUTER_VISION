import cv2

img =cv2.imread("person.jpg")


cv2.imshow("person",img)
cv2.waitKey(0)
cv2.destroyAllWindows( )