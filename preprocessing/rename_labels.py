import os

LABEL_FOLDER = './data/labels'

all_files = os.listdir(LABEL_FOLDER)

folders = list(filter(lambda filename: os.path.isdir(f'{LABEL_FOLDER}/{filename}'), all_files))
folders = list(map(lambda folder_name: int(folder_name), folders))
folders.sort()


for folder in folders:
    labels = os.listdir(f'{LABEL_FOLDER}/{folder}/')
    for label in labels:
        oldPath = f'{LABEL_FOLDER}/{folder}/{label}'
        frameNum = int(label.split('.')[0].split('_')[1])
        newPath = f'{LABEL_FOLDER}/{folder:02}{frameNum:03}.txt'
        os.rename(oldPath, newPath)
