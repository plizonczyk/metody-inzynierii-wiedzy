from csv import DictReader
import random
from pprint import pprint

from KNN.feature import Feature
from .som import SOM

som_params = {
    'matrix_size': 5,
    'initial_sigma': 5,
    'initial_gamma': 1,
    'alpha': 70,
}

teaching_limit = 150

data_file = 'KNN/data.txt'

features = []

with open(data_file, newline='') as data:
    reader = DictReader(data, delimiter='\t')
    for row in reader:
        features.append(Feature(row, 'class'))

teaching_limit = teaching_limit if teaching_limit < len(features) else len(features)
param_names = reader.fieldnames
param_names.remove('class')

som = SOM(param_names, som_params)

# randomize input
random.shuffle(features)
for feature in features[:teaching_limit]:
    som.teach(feature)

pprint(som.results)
