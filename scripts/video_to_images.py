import cv2

videoname = 'Video00002_ambient'
video = cv2.VideoCapture(f'./data/train/{videoname}.avi')
success, frame = video.read()
print(success)

i = 0
while success:
    cv2.imwrite(f'./data/train/{videoname}/frame_{i:03}.jpg', frame)
    success, frame = video.read()
    print(f'Converted frame {i}')
    i += 1

print(f'Converted {i} frames')

