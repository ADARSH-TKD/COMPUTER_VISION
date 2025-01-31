import cv2


f= cv2.CascadeClassifier(r"C:\Users\adarsh\AppData\Local\Programs\Python\Python312\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)  
while cap.isOpened(): 
    ret, frame = cap.read()
    if ret == True:
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        d=f.detectMultiScale(image= gray , scaleFactor=1.2, minNeighbors=2)

        for (x,y,w,h) in d:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.imshow("camera_my_friend", frame)
        if cv2.waitKey(25) & 0xFF == ord(' '):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
