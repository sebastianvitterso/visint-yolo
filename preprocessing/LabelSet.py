from typing import List
from Label import Label

class LabelSet():
    def __init__(self, labels:List['Label']):
        self.labels = labels
        
    def __str__(self):
        return f"<LabelSet len(labels)={len(self.labels)}>"
    def __repr__(self):
        return self.__str__()

    @classmethod
    def fromJsonImageLabelData(cls, imageLabelData:dict):
        if 'labels' not in imageLabelData: imageLabelData['labels'] = []
        bboxes = list(filter(lambda label: 'box2d' in label, imageLabelData['labels']))
        labels = list(map(lambda bbox: Label.fromJsonBbox(bbox), bboxes))
        return LabelSet(labels)

    @classmethod
    def loadFromFilePath(cls, file_path:str) -> 'LabelSet':
        with open(file_path) as file:
            labels = list(map(lambda line:Label.fromLabelLine(line.strip()), file.readlines()))
            return LabelSet(labels)

    def writeToFilePath(self, file_path:str):
        label_lines = list(map(lambda label:label.toLabelLine(), self.labels))
        label_file_text = '\n'.join(label_lines)
        with open(file_path, 'w') as file:
            file.write(label_file_text)