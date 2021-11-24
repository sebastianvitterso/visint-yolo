import cv2

videonames = [
    'Video00000_ambient',
    'Video00001_ambient',
    'Video00002_ambient',
]

for videoname in videonames:
    video = cv2.VideoCapture(f'./data/train/{videoname}.avi')
    success, frame = video.read()

    i = 0
    while success:
        cv2.imwrite(f'./data/train/images/{videoname}_frame_{i:06}.jpg', frame)
        success, frame = video.read()
        print(f'Converted frame {i}')
        i += 1

    print(f'Converted {i} frames')

