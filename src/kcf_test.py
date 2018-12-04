import cv2
import my_rect
import mat
import numpy as np
import kcftracker
import matplotlib.pyplot as plt
import skimage.io as io
import os

origin = os.path.abspath(os.path.dirname(os.getcwd()))
image_path = origin + '/test_data/girl/*.jpg'
groundtruth_path = origin + '/test_data/girl/groundtruth.txt'

def GetInput():
	image_rgb = io.ImageCollection(image_path)
	image_cv = []
	for i in range( len(image_rgb) ):
		image_cv.append(image_rgb[i][...,::-1])
	return image_cv

def GetRoi(num):
	file = open(groundtruth_path,"r")
	list_arr = file.readlines()
	for i in range( len(list_arr) ):
		list_arr[i] = list_arr[i].strip()
		list_arr[i] = list_arr[i].split(",")
	groundtruth = np.array(list_arr)
	groundtruth = groundtruth.astype(float)
	file.close()
	xMin = min(groundtruth[num,0], min(groundtruth[num,2], 
			min(groundtruth[num,4], groundtruth[num,6])))
	yMin = min(groundtruth[num,1], min(groundtruth[num,3], 
			min(groundtruth[num,5], groundtruth[num,7])))
	width = max(groundtruth[num,0], max(groundtruth[num,2], 
			max(groundtruth[num,4], groundtruth[num,6]))) - xMin
	height = max(groundtruth[num,1], max(groundtruth[num,3], 
			max(groundtruth[num,5], groundtruth[num,7]))) - yMin
	rect_result = my_rect.CVrect(xMin,yMin,width,height)
	return rect_result

if __name__=="__main__":
	img = GetInput()
	tracking = kcftracker.KCFTracker()
	if len(img) != 0:
		orig_image = mat.Mat.from_array(img[0])
		roi = GetRoi(0)
		tracking.init(roi, orig_image)
		cv2.rectangle(img[0][...,::-1], (roi.x,roi.y), (roi.x+roi.width,roi.y+roi.height), (0,255,0), 2)
		for i in range( 1, len(img) ):
			orig_image = mat.Mat.from_array(img[i])
			res = tracking.update(orig_image)
			cv2.rectangle(img[i][...,::-1], (res.x,res.y), (res.x+res.width,res.y+res.height), (0,255,0), 2)
			cv2.imshow("KCF_GPU", img[i])
			c = cv2.waitKey(0)
			if c == 27:
				break





