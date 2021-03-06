from csv import DictReader

from .feature import Feature
from .knn import KNN

data_file = 'KNN/data.txt'

features = []

with open(data_file, newline='') as data:
    reader = DictReader(data, delimiter='\t')
    for row in reader:
        features.append(Feature(row, 'class'))

    knn_classifier = KNN(features)
    result, __ = knn_classifier.cross_validate()
    print("Overall KNN accuracy:", result)
