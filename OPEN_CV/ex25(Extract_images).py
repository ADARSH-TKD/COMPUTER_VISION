import cv2
cap= cv2.VideoCapture("video2.mp4")
c=0
while True:
    ret,frame=cap.read()
    if ret==True:
        filename="C:\\Users\\adarsh\\Downloads\\OPEN CV\\image"+str(c)+".png"
        cv2.imwrite(filename,frame)
        c+=1
    else:
        break
    
cap.release()
cv2.destroyAllWindows()       
