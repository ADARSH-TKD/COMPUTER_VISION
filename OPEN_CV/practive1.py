import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,fr=cap.read()
    if ret ==True:
        fr=cv2.flip(fr,1)
        frame=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY )
        _, th = cv2.threshold(src=frame, thresh=200, maxval=255, type=cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        contours, hierarchy = cv2.findContours(image=th, mode=cv2.RETR_TREE, method=cv2.RETR_TREE, contours=None, hierarchy=None, offset=None)

        new_img= cv2.drawContours(image=fr, contours=contours, contourIdx=-1, color=(0,255,0), thickness=2)
        
        
        cv2.imshow("video",new_img)
        if cv2.waitKey(25) & 0xff == ord(" "):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()