import cv2
import numpy as np
class Trackobject(object):
	def __init__(self,scaling_factor=0.8):
		self.cap=cv2.VideoCapture(0)
		_,self.frame=self.cap.read()
		self.scaling_factor=scaling_factor
		self.frame=cv2.resize(self.frame,None,fx=self.scaling_factor,fy=self.scaling_factor,interpolation=cv2.INTER_AREA)
		cv2.namedWindow('Object Tracker')
		cv2.setMouseCallback('Object Tracker', self.mouse_event)
		self.selection=None
		self.drag_start=None
		self.tracking_state=0
	def mouse_event(self,event,x,y,flags,param):
		x,y=np.int16([x,y])
		if event == cv2.EVENT_LBUTTONDOWN:
			self.drag_start=(x,y)
			self.tracking_state=0
		if self.drag_start:
			if flags & cv2.EVENT_FLAG_LBUTTON:
				h,w=self.frame.shape[:2]
				xi,yi=self.drag_start
				x0,y0=np.maximum(0,np.minimum([xi,yi],[x,y]))
				x1,y1=np.minimum([w,h],np.maximum([xi,yi],[x,y]))
				self.selection=None
				if x1-x0 > 0 and y1-y0 > 0:
					self.selection=(x0,y0,x1,y1)
			else:
				self.drag_start=None
				if self.selection is not None:
					self.tracking_state=1
	def start_tracking(self):
		while True:
			_,self.frame=self.cap.read()
			self.frame=cv2.resize(self.frame,None,fx=self.scaling_factor,fy=self.scaling_factor,interpolation=cv2.INTER_AREA)
			vis=self.frame.copy()
			hsv=cv2.cvtColor(self.frame,cv2.COLOR_BGR2HSV)
			mask=cv2.inRange(hsv,np.array((0.,60.,32.)),np.array((180.,255.,255.)))	
			if self.selection:
				x0,y0,x1,y1=self.selection
				self.track_window=(x0,y0,x1-x0,y1-y0)
				roi_hsv=hsv[y0:y1,x0:x1]
				roi_mask=mask[y0:y1,x0:x1]
				hist=cv2.calcHist([roi_hsv],[0],roi_mask,[16],[0,180])
				cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX)			
				self.hist=hist.reshape(-1)
				vis_roi = vis[y0:y1, x0:x1]
				cv2.bitwise_not(vis_roi, vis_roi)
				vis[mask == 0] = 0
			if self.tracking_state == 1:
				self.selection = None
				hsv_backproj = cv2.calcBackProject([hsv],[0],self.hist,[0, 180],1)
				hsv_backproj &= mask
				term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)
				track_box,self.track_window = cv2.CamShift(hsv_backproj,self.track_window, term_crit)
				cv2.ellipse(vis, track_box, (0, 255, 0), 2)
			cv2.imshow('Object Tracker', vis)
			key=cv2.waitKey(5)
			if key==27:
				break
		cv2.destroyAllWindows()
			
if __name__=='__main__':
	Trackobject().start_tracking()

