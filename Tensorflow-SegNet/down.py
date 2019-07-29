from PIL import Image
import numpy as np
import cv2

p1 = './IBM/zaihou.jpg'
p2 = './IBM/0123.png'

w = 480 
h = 360 

#im1 = np.array(Image.open(p1))
#im2 = np.array(Image.open(p2))
im1 = cv2.imread(p1)
im2 = cv2.imread(p2)

im1 = cv2.resize(im1, (w, h))
im2 = cv2.resize(im2, (w, h))

print(im1.shape)
cv2.imwrite('disaster.png', im1)
cv2.imwrite('label.png', im2[:,:,0])

