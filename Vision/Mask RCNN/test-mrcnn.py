import mrcnn
import cv2

img = cv2.imread('straight_lines2.jpg')

result = mrcnn.annotate_image(img)

cv2.imshow('test' ,result)

cv2.waitKey(0)

