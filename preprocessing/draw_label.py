import cv2
import matplotlib.pyplot as plt

from LabelSet import LabelSet

IMAGE_PATH = './data/chevy.jpg'
LABEL_PATH = './data/chevy.txt'

image = cv2.cvtColor(cv2.imread(IMAGE_PATH), cv2.COLOR_BGR2RGB)
categories = ['biker', 'car', 'pedestrian', 'trafficLight', 'trafficLight-Green', 'trafficLight-GreenLeft', 'trafficLight-Red', 'trafficLight-RedLeft', 'trafficLight-Yellow', 'trafficLight-YellowLeft', 'truck']
labelSet = LabelSet.loadFromFilePath(LABEL_PATH)
for label in labelSet.labels:
    image = cv2.rectangle(image, (label.left, label.top), (label.right, label.bottom), (255,0,0), 1)
    image = cv2.putText(image, categories[label.category], (label.left, label.top), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 1, cv2.LINE_AA)


plt.figure()
plt.imshow(image)
plt.show()


