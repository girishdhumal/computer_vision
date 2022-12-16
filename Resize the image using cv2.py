import cv2
img = cv2.imread("a.jpeg")
resize= cv2.resize(img,(200,200))
cv2.imshow('window',resize)
cv2.waitKey()
cv2.distroyAllWindows()