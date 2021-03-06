from csv import DictReader

from KNN.feature import Feature
from .node import Node


class AGDS(object):
    def __init__(self, data_file):
        self.root = Node('param')
        self.id_nodes = {}
        features = []

        # read features and create objects
        with open(data_file, newline='') as data:
            reader = DictReader(data, delimiter='\t')
            for row in reader:
                features.append(Feature(row, 'class'))

        # create first level of tree - parameter names
        for fieldname in reader.fieldnames:
            self.root.add(fieldname, Node(fieldname))

        # fill values with id-nodes already linked
        for feature in features:
            id_node = Node(feature.feature_id)
            self.id_nodes[feature.feature_id] = id_node
            for key, value in feature.data_dict.items():
                self.root.get(key).add(key, Node(value), final_node=id_node)
            self.root.get('class').add(feature.feature_class, Node(feature.feature_class), final_node=id_node)
