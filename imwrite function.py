import cv2
img = cv2.imread('h.png')
cv2.imwrite('save.jpg',img)
print("file saved successfully.")