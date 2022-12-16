import cv2
#from google.colab.patches import cv2_imshow
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('test4.jpeg')
cv2.putText(img=img, text="SHANTANU",org=(100, 250), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 0, 0),thickness=1)
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)
# Display the output
cv2.imshow('window',img)
cv2.waitKey(0)