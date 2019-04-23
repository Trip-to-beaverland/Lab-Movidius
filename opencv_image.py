from __future__ import division
import cv2


img = cv2.imread('./sample_img/doge.jpg')

#screen_res = 1280, 720
#scale_width = screen_res[0] / img.shape[1]
#scale_height = screen_res[1] / img.shape[0]
#scale = min(scale_width, scale_height)
window_width = int(img.shape[1])
window_height = int(img.shape[0])

#CONVERTING
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#CROPPING
cv2.rectangle(img, (20,50), (120,150), (0,255,0), 3)
#cropped = img[50:150,20:120]

cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst_rt', window_width, window_height)

cv2.imshow('dst_rt', img)
cv2.waitKey(0)
cv2.destroyAllWindows()