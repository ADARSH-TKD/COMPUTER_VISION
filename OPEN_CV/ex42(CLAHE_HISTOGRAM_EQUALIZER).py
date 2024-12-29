import cv2
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
img = cv2.imread("clahe.jpg")

# Crop the image
img = img[30:340, 0:500]

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
e = cv2.equalizeHist(gray_img)

# Apply CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_img =clahe.apply(gray_img)

# Calculate histograms
h1=cv2.calcHist([gray_img],[0],None,[256],[0,256])
h2=cv2.calcHist([e],[0],None,[256],[0,256])
h3=cv2.calcHist([clahe_img],[0],None,[256],[0,256])

# Plot histograms

plt.figure(figsize=(5,5))
plt.subplot(3,1,1)
plt.plot(h1,color="blue")
plt.title("Original Image",color="blue")

plt.subplot(3,1,2)
plt.plot(h2,color="green")
plt.title("Equalized Image",color="green")

plt.subplot(3,1,3) 
plt.plot(h3,color="red")
plt.title("CLAHE Image",color="red")

plt.show() # Display the histograms

# Display the result
h=np.hstack((gray_img,e,clahe_img))
cv2.putText(h, "Original Image", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(h,"Equalized Image",(460,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
cv2.putText(h,"CLAHE Image",(900,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
cv2.imwrite("EQUALIZATION.jpg",h)
cv2.imshow("Equalized Image", h)
cv2.waitKey(0)
cv2.destroyAllWindows()
