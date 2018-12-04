import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = '/home/lancer/GPU_KCF/test_data/girl/00000001.jpg'
img = cv2.imread(image_path)
# img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
# cv2.rectangle(img,(20,20),(411,411),(55,255,155),5)
cv2.imshow('brg',img)
print("hello")
cv2.waitKey();