import os, sys, time, datetime, random
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torch.autograd import Variable
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import torch
from PIL import Image
import torchvision
import numpy as np

import colorsys
import random
import cv2
N = 100
HSV_tuples = [(x/N, 1, 1) for x in range(N)]
RGB_tuples = list(map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples))
RGB_tuples = list(map(lambda x: (x[0] * 255, x[1] * 255, x[2] * 255), RGB_tuples))
random.shuffle(RGB_tuples)


PATH = "faster_rcnn_r50_fpn_3x_bdd100k.pth"
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
checkpoint = torch.load(PATH, map_location=torch.device('cpu'))
model.load_state_dict(checkpoint, strict=False)
model.eval()

def detect_image(img):
    transform = transforms.ToTensor()
    input = transform(img)

    input = input.unsqueeze(0)

    model.eval()

    output = model(input)
    return output

def add_labels(img, detections):
    img = np.array(img)

    for label, category_id, conf in zip(detections[0]['boxes'], detections[0]['labels'], detections[0]['scores']):
        if conf > 0.25:
            img = cv2.rectangle(img, (int(label[0]), int(label[1])), (int(label[2]), int(label[3])), RGB_tuples[category_id.item()], 1)
    return img

# img_path = "bdd.jpg"
# prev_time = time.time()
# img = Image.open(img_path)
# detections = detect_image(img)
# inference_time = datetime.timedelta(seconds=time.time() - prev_time)
# print ('Inference Time: %s' % (inference_time))
# img = add_labels(img, detections)
# plt.imshow(img)
# plt.show()

INPUT_FOLDER = 'Video00001'
OUTPUT_FOLDER = 'Video00001_pred'
VIDEO_NUMBER = 1

BASE_FILENAME = f'Video{VIDEO_NUMBER:05}'
AMBIENT_FILEPATH =   f'{INPUT_FOLDER}/{BASE_FILENAME}_ambient.avi'
ambientCapture = cv2.VideoCapture(AMBIENT_FILEPATH)
out = cv2.VideoWriter(f'{OUTPUT_FOLDER}/ambient01.avi', cv2.VideoWriter_fourcc(*'XVID'), 30.0, (1024,128))

assert ambientCapture.isOpened(), 'Error: ambientCapture'

frameNum = 0

# Read until video is completed
while(ambientCapture.isOpened()):
    aSuccess, frame = ambientCapture.read()

    if not (aSuccess):
        break
    
    img = frame.copy()

    prev_time = time.time()
    detections = detect_image(frame)
    labeled_img = add_labels(frame, detections)
    inference_time = datetime.timedelta(seconds=time.time() - prev_time)
    print (f'Inference Time: {inference_time}. [{frameNum}/ca 100]')

    out.write(labeled_img)
    
    
    frameNum += 1


# When everything done, release the video capture object
ambientCapture.release()
out.release()
