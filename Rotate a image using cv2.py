#import cv2
#img = cv2.imread(r"C:\Users\Vikas\Downloads\simple.jpg")
#rotate = cv2.rotate(img,1)
#cv2.imshow("window1",rotate)
#cv2.waitKey()
#cv2.distroyAllWindows()


import cv2
image = cv2.imread(r"C:\Users\Vikas\Downloads\simple.jpg")
height, width = image.shape[:2]
# get the center of the image
center_x, center_y = (width/2, height/2)
# rotate the image by 60 degrees counter-clockwise around the center of the image
M = cv2.getRotationMatrix2D((center_x, center_y), 60, 1.0)
rotated_image = cv2.warpAffine(image, M, (width, height))
cv2.imshow("Rotated image", rotated_image)
cv2.waitKey(0)
cv2.distroyAllWindows()
