import os
from LabelSet import LabelSet

# visint_labels = ['car', 'truck', 'bus', 'motorcycle', 'bicycle', 'scooter', 'person', 'rider']  # original
visint_labels = ['car', 'truck', 'car', 'car', 'biker', 'biker', 'pedestrian', 'biker']  # revised, to only contain ones represented in COCO

udacity_labels = ['biker', 'car', 'pedestrian', 'trafficLight', 'trafficLight-Green', 
                  'trafficLight-GreenLeft', 'trafficLight-Red', 'trafficLight-RedLeft', 
                  'trafficLight-Yellow', 'trafficLight-YellowLeft', 'truck'] 

label_index_mapping = {}
for visint_label_index, visint_label in enumerate(visint_labels):
    coco_label_index = udacity_labels.index(visint_label)
    label_index_mapping[visint_label_index] = coco_label_index
    print(f'{visint_label} ({visint_label_index} -> {coco_label_index})')

######################################################################################################################

INPUT_LABEL_FOLDER = './data/labels'
OUTPUT_LABEL_FOLDER = './data/labels_for_udacity'

label_files = os.listdir(INPUT_LABEL_FOLDER)

for label_file in label_files:
    labelSet = LabelSet.loadFromFilePath(f'{INPUT_LABEL_FOLDER}/{label_file}')

    for label in labelSet.labels:
        # print(visint_labels[label.category], label.category, label_index_mapping[label.category])
        label.category = label_index_mapping[label.category]

    labelSet.writeToFilePath(f'{OUTPUT_LABEL_FOLDER}/{label_file}')

