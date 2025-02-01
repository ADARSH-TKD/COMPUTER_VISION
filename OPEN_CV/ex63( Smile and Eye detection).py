import cv2
c1 = cv2.CascadeClassifier(r"C:\Users\adarsh\AppData\Local\Programs\Python\Python312\Lib\site-packages\cv2\data\haarcascade_eye.xml")
c2 = cv2.CascadeClassifier(r"C:\Users\adarsh\AppData\Local\Programs\Python\Python312\Lib\site-packages\cv2\data\haarcascade_smile.xml")
cap=cv2.VideoCapture(0)
while True:
    ret ,frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1)
        g = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        e1 = c1.detectMultiScale(g,1.2,2)
        e2 = c2.detectMultiScale(g,5,10) // error
        for (x,y,w,h) in e1:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)        
        for (x,y,w,h) in e2:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.imshow("Eye Detection",frame)
        if cv2.waitKey(25) & 0xFF == ord(' '):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()