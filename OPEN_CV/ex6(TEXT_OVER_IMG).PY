import cv2


im_get = cv2.imread("love.jpg")
rs = cv2.resize(im_get, (300, 500))
text = "LOVE me baby"
org = (50, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)
thickness = 3
lineType = cv2.LINE_AA
t = cv2.putText(rs, text, org, font, fontScale, color, thickness, lineType,False)
t2 = cv2.putText(t, "LOVE me baby", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3, cv2.LINE_AA,True)

cv2.imshow("image", t2)
cv2.waitKey(0)
cv2.destroyAllWindows()
