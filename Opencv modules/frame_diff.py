import cv2
import time
def frame_diff(prev,curr,next):
	diff1=cv2.absdiff(next,curr)
	diff2=cv2.absdiff(curr,prev)
	return cv2.bitwise_and(diff1,diff2)

def get_frame(cap,scaling_factor):
	w,frame=cap.read()
	frame=cv2.resize(frame,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
	gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
	return gray

cap=cv2.VideoCapture(0)
scaling_factor=2
prev=get_frame(cap,scaling_factor)
curr=get_frame(cap,scaling_factor)
next=get_frame(cap,scaling_factor)
while True:
	cv2.imshow('Object Movement',frame_diff(prev,curr,next))
	prev=curr
	curr=next
	next=get_frame(cap,scaling_factor)
	key=cv2.waitKey(10)
	if key==27:
		break
cv2.destroyAllWindows()
