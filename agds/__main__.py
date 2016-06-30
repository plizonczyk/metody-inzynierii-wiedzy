from pprint import pprint
from csv import DictReader

from KNN.feature import Feature
from .node import Node

data_file = 'agds/data.txt'

root = Node('param')
features = []

# read features and create objects
with open(data_file, newline='') as data:
    reader = DictReader(data, delimiter='\t')
    for row in reader:
        features.append(Feature(row, 'class'))

# create first level of tree - parameter names
for fieldname in reader.fieldnames:
    root.add(fieldname, Node(fieldname))

# fill values with id-nodes already linked
for feature in features:
    id_node = Node(feature.feature_id)
    for key, value in feature.data_dict.items():
        root.get(key)[0].add(key, Node(value), final_node=id_node)

import ipdb; ipdb.set_trace()
