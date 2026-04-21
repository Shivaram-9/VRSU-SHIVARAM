import cv2

img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(gray, None)

output = cv2.drawKeypoints(gray, kp, img)

cv2.imshow("SIFT Keypoints", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
