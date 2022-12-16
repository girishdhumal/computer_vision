import cv2
#from google.colab.patches import cv2_imshow
img = cv2.imread("a.jpeg") # Read image
# Setting All parameters
t_lower = 10 # Lower Threshold
t_upper = 100 # Upper threshold
aperture_size = 5 # Aperture size
# Applying the Canny Edge filter
# with Custom Aperture Size
edge = cv2.Canny(img, t_lower, t_upper, apertureSize=aperture_size)
cv2_imshow('window1',img)
cv2_imshow('window2',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()