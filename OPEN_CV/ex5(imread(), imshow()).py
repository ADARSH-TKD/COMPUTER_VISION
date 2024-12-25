import cv2
import numpy as np

# Load images with different modes
a = cv2.imread("love.jpg", 0)   # Grayscale
c = cv2.imread("love.jpg", -1) # Includes alpha channel
b = cv2.imread("love.jpg", 1)  # Color

# Resize all images to the same dimensions
rs = cv2.resize(a, (300, 400))
rs2 = cv2.resize(b, (300, 400))
rs3 = cv2.resize(c, (300, 400))

# Convert grayscale to 3 channels
# rs = cv2.cvtColor(rs, cv2.COLOR_GRAY2BGR)

# Stack images horizontally
img = np.hstack((rs, rs2, rs3))

# Display the combined image
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print shape of the grayscale image
print(a.shape)
print(c.shape)
print(b.shape )