import cv2


image = cv2.imread("path to image")
image_copy = image

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow("input_image", image_copy)
cv2.imshow("contour_detected_image", image)
cv2.waitKey(0)
