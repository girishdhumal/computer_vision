import matplotlib.pyplot as plt
from skimage import data
from skimage.color import rgb2hsv
import cv2
path = r"C:\Users\Vikas\Downloads\simple.jpg"
img = cv2.imread(path)
rgb_img = img
hsv_img = rgb2hsv(rgb_img)
value_img = hsv_img[:, :, 2]
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 2))
ax0.imshow(rgb_img)
ax0.set_title("Original image")
ax0.axis('off')
ax1.imshow(value_img)
ax1.set_title("Image converted to HSV channel")
ax1.axis('off')
fig.tight_layout()