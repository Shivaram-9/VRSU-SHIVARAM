import cv2

cap = cv2.VideoCapture('video.mp4')

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % 30 == 0:
        cv2.imwrite(f"frame_{frame_count}.jpg", frame)

    frame_count += 1

cap.release()
print("Frames extracted successfully")
