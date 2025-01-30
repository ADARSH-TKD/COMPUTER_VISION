import cv2
img = cv2.resize(cv2.imread(r"C:\Users\adarsh\Downloads\GREEN AI\PROJECT\FASHION-MNIST-CLASSIFICATION\tree_dataset\testing\2_post-SW\DJI_20241229133644_0200_V.JPG"),(1500,790))
cv2.imwrite("greenAI20.jpg",img)

