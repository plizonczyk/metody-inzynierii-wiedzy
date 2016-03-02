import random

import math

import sys

import itertools


class KNN(object):
    def __init__(self, features):
        self.features = features
        self.features_lists_by_class = self._create_lists()
        self.folds = None

    def _create_lists(self):
        result = {}
        for feature in self.features:
            if feature.feature_class in result:
                result[feature.feature_class].append(feature.values)
            else:
                result[feature.feature_class] = [feature.values]
        return result

    def cross_validate(self, k=3):
        """
        Test set using k-fold cross validation
        :param k: how many folds to create
        """
        self.folds = self._create_folds(k)

        itertools.permutations()

    def _create_folds(self, k):
        """
        Divides given list into k lists of equal (or almost equal if indivisible) number of elements
        :return: list of tuples (feature_class, list of k-lists)
        """

        result = []
        for feature_class, features in self.features_lists_by_class.items():
            randomized = random.sample(features, len(features))

            chunk_size = math.ceil(len(randomized)/k)
            last_chunk_size = len(randomized) - chunk_size * (k-1)

            lists = [randomized[i*chunk_size: (i+1)*chunk_size] for i in range(k-1)]
            lists.append(randomized[-last_chunk_size:])
            try:
                assert sum([len(l) for l in lists]) == len(randomized)
            except AssertionError:
                print("Chunks size don't sum up to length of original list")
                sys.exit()

            result.append((feature_class, lists))
        return result
