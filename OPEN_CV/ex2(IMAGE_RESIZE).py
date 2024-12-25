import cv2 
a= cv2.imread("car.jpg")
rs = cv2.resize(a,(300,400))
cv2.imshow("car",rs)
cv2.waitKey(0)
cv2.destroyAllWindows()