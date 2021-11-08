import cv2

input_folder = './data/train/'
videonames = [
    'Video00000_ambient',
    'Video00001_ambient',
    'Video00002_ambient',
]

def input_file(videoname):
    return f'./data/train/{videoname}.avi'

def output_folder(videoname):
    return f'./data/train/{videoname}/'


for videoname in videonames:
    video = cv2.VideoCapture(input_file(videoname))
    success, frame = video.read()

    i = 0
    while success:
        cv2.imwrite(f'{output_folder(videoname)}/frame_{i:03}.jpg', frame)
        success, frame = video.read()
        print(f'Converted frame {i}')
        i += 1

    print(f'Converted {i} frames')

