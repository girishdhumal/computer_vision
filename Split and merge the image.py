import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Vikas\Downloads\simple.jpg")
#spliting part
(B, G, R) = cv2.split(img)
cv2.imshow('window',R)
cv2.imshow('windows1',G)
cv2.imshow('windows2',B)
#merging part
merged = cv2.merge([B, G, R])
cv2.imshow('windows4',merged)
cv2.waitKey(0)
cv2.distroyAllWindows()