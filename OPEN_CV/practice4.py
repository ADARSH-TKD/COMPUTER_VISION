import cv2
import numpy as np

# Load images
img = cv2.imread("thor.jpg")
demo = cv2.imread("demo.jpg")

# Resize for consistency (optional, based on your image sizes)
img = cv2.resize(img, (400, 300))
demo = cv2.resize(demo, (400, 300))

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_demo = cv2.cvtColor(demo, cv2.COLOR_BGR2HSV)

# Calculate histogram for the demo image
hist = cv2.calcHist([hsv_demo], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Back projection
mask = cv2.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)

# Apply filtering
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask = cv2.filter2D(mask, -1, kernel)

# Threshold the mask
_, th = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY)

# Morphological operations to refine the mask
k = np.ones((5, 5), np.uint8)
op = cv2.morphologyEx(th, cv2.MORPH_OPEN, k, iterations=1)

# Convert the mask to 3 channels for bitwise operation
mask_3ch = cv2.merge((op, op, op))

# Apply mask on the original image
res = cv2.bitwise_and(img, mask_3ch)

# Display results
cv2.imshow("Result", res)
cv2.imshow("Original Image", img)
cv2.imshow("Refined Mask", op)
cv2.waitKey(0)
cv2.destroyAllWindows()
