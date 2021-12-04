import os
from LabelSet import LabelSet

# visint_labels = ['car', 'truck', 'bus', 'motorcycle', 'bicycle', 'scooter', 'person', 'rider']  # original
visint_labels = ['car', 'truck', 'bus', 'motorcycle', 'bicycle', 'skateboard', 'person', 'person']  # revised, to only contain ones represented in COCO

coco_labels = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
        'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
        'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
        'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
        'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
        'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
        'hair drier', 'toothbrush']  # class names

label_index_mapping = {}
for visint_label_index, visint_label in enumerate(visint_labels):
    coco_label_index = coco_labels.index(visint_label)
    label_index_mapping[visint_label_index] = coco_label_index
    print(f'{visint_label} ({visint_label_index} -> {coco_label_index})')

######################################################################################################################

INPUT_LABEL_FOLDER = './data/labels'
OUTPUT_LABEL_FOLDER = './data/labels_for_coco'

label_files = os.listdir(INPUT_LABEL_FOLDER)

for label_file in label_files:
    labelSet = LabelSet.loadFromFilePath(f'{INPUT_LABEL_FOLDER}/{label_file}')

    for label in labelSet.labels:
        # print(visint_labels[label.category], label.category, label_index_mapping[label.category])
        label.category = label_index_mapping[label.category]

    labelSet.writeToFilePath(f'{OUTPUT_LABEL_FOLDER}/{label_file}')

