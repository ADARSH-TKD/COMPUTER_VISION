import cv2
import numpy as np 
import matplotlib.pyplot as plt 

# Create a black image
black = np.zeros((400, 400, 3), np.uint8)* 255  # Multiplying by 255 is unnecessary

# Create a white image
white = np.ones((400, 400, 3), np.uint8) * 255  # Ensures all values are 255

hist_black=cv2.calcHist([black],[0],None,[256],[0,256])
hist_white=cv2.calcHist([white],[0],None,[256],[0,256])

plt.plot(hist_black, label="Black Image", color='black')
plt.plot(hist_white, label="White Image", color='green')
plt.show()
# Display the images
cv2.imshow("Black Image", black)
cv2.imshow("White Image", white)
cv2.waitKey(0)
cv2.destroyAllWindows()
