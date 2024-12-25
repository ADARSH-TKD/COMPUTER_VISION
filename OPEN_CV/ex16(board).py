import cv2
import numpy as np 

# Load the image and resize it
image = cv2.imread("car.jpg")
a = cv2.resize(image, (300, 400))

# Add a border around the image
b = cv2.copyMakeBorder(src=a, top=10, bottom=10, left=10, right=10,borderType=cv2.BORDER_REFLECT)
b = cv2.resize(image, (300, 400))


# Add a border around the image
c = cv2.copyMakeBorder(src=a, top=10, bottom=10, left=10, right=10, borderType=cv2.BORDER_CONSTANT, value=[255,0,0])
c = cv2.resize(image, (300, 400))


h = np.hstack((a, b, c))
# Display the resulting image
cv2.imshow("Image with Border", h)
cv2.waitKey(0)
cv2.destroyAllWindows()

