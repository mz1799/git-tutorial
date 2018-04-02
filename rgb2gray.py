import cv2
import numpy as np

img = cv2.imread('test.jpg')
img_f = img.astype("float32")
size = img.shape
grayimg = np.zeros((size[0],size[1]))
for i in range(size[0]):
    for j in range(size[1]):
        grayimg[i,j] = (img_f[i,j,0] + img_f[i,j,1] + img_f[i,j,2])/3
cv2.imshow('image',grayimg)
cv2.waitKey(0)

        
    
