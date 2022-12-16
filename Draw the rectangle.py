import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Vikas\Downloads\simple.jpg")
cv2.rectangle(img,(0,0),(200,200),(0,0,255),thickness = cv2.FILLED)
cv2.imshow("window",img)
cv2.waitKey(0)
cv2.distroyAllWindows()