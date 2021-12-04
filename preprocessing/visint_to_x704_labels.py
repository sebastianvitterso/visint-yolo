import os
from LabelSet import LabelSet

# visint_labels = ['car', 'truck', 'bus', 'motorcycle', 'bicycle', 'scooter', 'person', 'rider']  # original
visint_labels = ['vehicle', 'vehicle', 'bus', 'vehicle', 'cyclist', 'cyclist', 'pedestrian', 'pedestrian']  # revised, to only contain ones represented in x704

x704_labels = ['vehicle', 'pedestrian', 'construction', 'bus', 'cyclist']

label_index_mapping = {}
for visint_label_index, visint_label in enumerate(visint_labels):
    x704_label_index = x704_labels.index(visint_label)
    label_index_mapping[visint_label_index] = x704_label_index
    print(f'{visint_label} ({visint_label_index} -> {x704_label_index})')

######################################################################################################################

INPUT_LABEL_FOLDER = './data/labels'
OUTPUT_LABEL_FOLDER = './data/labels_for_x704'

label_files = os.listdir(INPUT_LABEL_FOLDER)

for label_file in label_files:
    labelSet = LabelSet.loadFromFilePath(f'{INPUT_LABEL_FOLDER}/{label_file}')

    for label in labelSet.labels:
        # print(visint_labels[label.category], label.category, label_index_mapping[label.category])
        label.category = label_index_mapping[label.category]

    labelSet.writeToFilePath(f'{OUTPUT_LABEL_FOLDER}/{label_file}')

