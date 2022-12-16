import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Vikas\Downloads\simple.jpg")
cv2.putText(img=img, text="AMIT",org=(100, 250), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255,255,255),thickness=5)
cv2.imshow("windows",img)
cv2.waitKey()
cv2.distroyAllWindows()