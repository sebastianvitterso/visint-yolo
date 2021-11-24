import os
import shutil

indexes = [
    0,
    # 1,
    2,
]

def label_folder(index):
    return f'./data/annotations/0{index}_yolo/obj_train_data'

def input_filepath(index, filename):
    return f'{label_folder(index)}/{filename}'

def output_filepath(index, filename):
    return f'./data/train/labels/Video0000{index}_ambient_{filename}'

for index in indexes:
    folder = label_folder(index)
    for label_file in os.listdir(folder):
        print(input_filepath(index, label_file), output_filepath(index, label_file))
        shutil.copy2(input_filepath(index, label_file), output_filepath(index, label_file))

