import cv2
img1= cv2.resize(cv2.imread("love.jpg"),(400,600))
img2= cv2.resize(cv2.imread("car.jpg"),(400,600))
# add = img1 + img2
new=cv2.addWeighted(src1=img1, alpha=1, src2=img2, beta=1, gamma=1, dst=None, dtype=None)
# sub= imag1-img2
new2=cv2.substract(src1=img1, src2=img2, dst=None, mask=None, dtype=None)

cv2.imshow("image",new)
cv2.imshow("image",new2)

cv2.waitKey(0)
cv2.destroyAllWindows()
