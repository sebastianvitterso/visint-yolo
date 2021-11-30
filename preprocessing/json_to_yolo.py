import json

from LabelSet import LabelSet
from Label import categories

TYPE = 'val' 
JSON_FOLDER = './data/json_labels'
OUTPUT_FOLDER = f'{JSON_FOLDER}/{TYPE}'
INPUT_FILE = f'{JSON_FOLDER}/det_{TYPE}.json'

with open(INPUT_FILE) as file:
    data = json.load(file)

for i, imageLabelData in enumerate(data):
    labelSet = LabelSet.fromJsonImageLabelData(imageLabelData)
    filename = imageLabelData['name'].split('.')[0]
    filepath = f'{OUTPUT_FOLDER}/{filename}.txt'
    labelSet.writeToFilePath(filepath)
    print(f'Wrote labelset {filename}.txt [{i+1}/{len(data)}]', end='\r')

print('\n', categories)