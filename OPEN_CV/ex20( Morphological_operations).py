import cv2
import numpy as np

# Read the image
img = cv2.imread("mp.png")

# Define the kernel (structuring element)
o = np.ones((5, 5), np.uint8)  # A 5x5 matrix of ones
print(o)

# Erosion
erosion = cv2.erode(img, o, iterations=1)

# Dilation
dilation = cv2.dilate(img, o, iterations=1)

# Stack the images horizontally for comparison
# Convert to the same size if necessary
h = np.hstack((img, erosion, dilation))

# Display the result
cv2.imshow("Morphological Operations", h)
cv2.waitKey(0)
cv2.destroyAllWindows()
