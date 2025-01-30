import cv2
cap=cv2.VideoCapture(0)
while True:
    ret , frame =cap.read()
    if ret == True:
        cv2.imshow("windeo",frame)
        if cv2.waitKey(25) and 0xff ==ord('p'):
            break
    else:
        break
cap.re    
    
    
    