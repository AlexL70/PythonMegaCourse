# To install opencv run the following command
# pip install opencv-python
import cv2

array = cv2.imread("files/image.png")
print(array.shape)
print(array)