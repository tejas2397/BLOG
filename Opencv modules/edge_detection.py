import cv2

img = cv2.imread('path to image',0)
edges = cv2.Canny(img,100,200)

cv2.imshow("input_image", img)
cv2.imshow("edge_detection", edges)
cv2.waitKey(0)

