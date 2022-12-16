import cv2
img = cv2.imread('a.jpeg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('window',img1)
print('type of image is: ',img.dtype)
print('Dimension of image is: ',img.size)
print('Shape of image is: ',img.shape)