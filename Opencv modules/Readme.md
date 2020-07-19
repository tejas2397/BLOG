Run back_sub.py as python3 back_sub.py to subtract the background from the current frameThe output contains two windows one the original frame and the other contains the background subtracted frame. With the help of backgoundsubtractor class in openv this implementation is done. It identifies the background using the first n number of terms initialised by the variable history.

Run frame_diff.py as python frame_diff.py to get the difference between two consecutive frames. if the video is still or unmoved there is obvioulsy no difference between the frame leading to black screen. The program is used to track the movement of the object.

Run sketch.py to get a sketch of an input image. Along with that there are different methods/filters used like gaussian filter,grayscale,inverting etc.

Run cartoon.py to get a cartooned image from an input image.It also contains code to different methods like upsampling & downsampling an image,median blur and adaptive thresholding. 

Run contour_detection.py to detect the contours of the objects in the image.

Run edge_detection.py to detect the edges of the objects in the image.
