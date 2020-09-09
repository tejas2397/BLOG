import cv2
import numpy as np
def start_tracking():
	cap=cv2.VideoCapture(0)
	scaling_factor=0.8
	num_track=5
	num_skip=2
	track_path=[]
	frame_index=0
	tracking_params = dict(winSize = (11,11), maxLevel = 2,criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10, 0.03))
	while True:
		w,frame=cap.read()
		frame=cv2.resize(frame,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
		frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		output_img=frame.copy()
		if len(track_path)>0:
			prev,curr=prev_gray,frame_gray
			feature_points_0 = np.float32([tp[-1] for tp in track_path]).reshape(-1, 1, 2)
			feature_points_1, _, _ = cv2.calcOpticalFlowPyrLK(prev, curr, feature_points_0,None, **tracking_params)
			feature_points_0_rev, _, _ = cv2.calcOpticalFlowPyrLK(curr, prev, feature_points_1,None, **tracking_params)
			diff_feature_points = abs(feature_points_0 - feature_points_0_rev).reshape(-1, 2).max(-1)
			good_points=diff_feature_points<1
			new_track_paths=[]
			for tp, (x, y), good_points_flag in zip(track_path,feature_points_1.reshape(-1, 2), good_points):
				if not good_points_flag:
					continue
				tp.append((x,y))
				if len(tp) > num_track:
					del tp[0]
				new_track_paths.append(tp)	
				cv2.circle(output_img,(x,y),3,(0,255,0),-1)
			track_paths=new_track_paths	
			cv2.polylines(output_img,[np.int32(tp) for tp in track_path], False, (0, 150, 0))
		if not frame_index % num_skip:
			mask = np.zeros_like(frame_gray)
			mask[:] = 255
			for x, y in [np.int32(tp[-1]) for tp in track_path]:
				cv2.circle(mask, (x, y), 6, 0, -1)
			feature_points = cv2.goodFeaturesToTrack(frame_gray,mask = mask, maxCorners = 500, qualityLevel = 0.3,minDistance = 7, blockSize = 7)
			if feature_points is not None:
				for x, y in np.float32(feature_points).reshape(-1, 2):
					track_path.append([(x, y)])
		frame_index += 1
		prev_gray = frame_gray		
		cv2.imshow('Optical Flow', output_img)
		c = cv2.waitKey(1)
		if c == 27:
			break

if __name__ == '__main__':
	start_tracking()
	cv2.destroyAllWindows()

