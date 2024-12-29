import cv2
import matplotlib.pyplot as plt
import numpy as np 

# Read and resize the image
leaf = cv2.resize(cv2.imread("leaf2.jpg"), (400, 400))

# Convert to grayscale
h1 = cv2.cvtColor(leaf, cv2.COLOR_BGR2GRAY)

# Calculate the histogram
# hist = cv2.calcHist(images=[leaf], channels=[0], mask=None, histSize=[255], ranges=[0, 255])

# Plot the histogram
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Pixel Intensity")
# plt.ylabel("Frequency")
# plt.plot(hist)
# plt.xlim([0, 256])  # Set limits for the x-axis
# plt.show()

# otsu's thresholding
_, th = cv2.threshold(src=h1, thresh=120, maxval=255, type=cv2.THRESH_BINARY + cv2.THRESH_OTSU)

hist_gray = cv2.calcHist(images=[h1], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
hist_otsu = cv2.calcHist(images=[th], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

# Plot histograms
plt.figure()
plt.title("Histograms of Grayscale and Otsu Thresholded Images")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(hist_gray, label="Grayscale Image", color='blue')
plt.plot(hist_otsu, label="Otsu Thresholded Image", color='red')
plt.xlim([0, 256])  # Set limits for the x-axis
plt.legend()
plt.show()
# Print the shape of the grayscale image
print("Shape of the grayscale image:", h1.shape)

# Display the grayscale image
h=np.hstack((h1,th))

cv2.imshow("OTSU", h)
cv2.waitKey(0)
cv2.destroyAllWindows()
