import cv2
import os

list_name = os.listdir(r"C:\Users\adarsh\Downloads\OPEN CV\image")
for name in list_name:
    path="C:\\Users\\adarsh\\Downloads\\OPEN CV\\image"
    img_name = path + "\\" + name 
    img = cv2.imread(img_name)
    img=cv2.resize(img,(500,600))
    cv2.imshow("image",img)
    cv2.waitKey(0)
cv2.destroyAllWindows()