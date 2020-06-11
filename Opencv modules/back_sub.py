import cv2
import numpy as np
def get_frame(cap,scaling_factor):
	w,frame=cap.read()
	frame=cv2.resize(frame,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
	return frame

cap=cv2.VideoCapture(0)
scaling_factor=0.8
bg_sub=cv2.createBackgroundSubtractorMOG2()
history=100
learning_rate=1.0/history
while True:
	frame=get_frame(cap,scaling_factor)
	mask=bg_sub.apply(frame,learningRate=learning_rate)
	mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
	cv2.imshow('input',frame)
	cv2.imshow('output',mask & frame)
	key=cv2.waitKey(10)
	if key==27:
		break
cv2.destroyAllWindows()
