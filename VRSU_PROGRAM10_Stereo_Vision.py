import cv2

left = cv2.imread('left.png', 0)
right = cv2.imread('right.png', 0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(left, right)

cv2.imshow("Depth Map", disparity)
cv2.waitKey(0)
cv2.destroyAllWindows()
