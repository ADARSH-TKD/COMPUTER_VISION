import cv2

cap = cv2.VideoCapture("vehicle.mp4")
while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        car = cv2.CascadeClassifier(r"C:\Users\adarsh\AppData\Local\Programs\Python\Python312\Lib\site-packages\cv2\data\haarcascade_car.xml")
        
        cars = car.detectMultiScale(gray, 1.1, 1)
        
        for (x,y,w,h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        
        cv2.imshow("vehicle", gray)  
        if cv2.waitKey(25) & 0xFF == ord(" "):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()