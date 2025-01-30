img = cv2.imread("shape.png")
gr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gr = np.float32(gr)
res = cv2.cornerHarris(src=gr, blockSize=2, ksize=3, k=0.04, dst=None, borderType=None)
res = cv2.dilate(res,None)

img[res>0.01*res.max()]=[0,0,255]