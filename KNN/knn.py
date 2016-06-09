import random
import math
import sys
import itertools
from pprint import pprint


class KNN(object):
    def __init__(self, features):
        self.features = features
        self.folds = None

    def knn(self, validation_features, test_features, k=3):
        pass

    def cross_validate(self, method=knn, n=3, k=3):
        """
        Test set using n-fold cross validation with kNN method
        :param method: method to use (knn or weighted_knn)
        :param n: how many folds to create
        :param k: parameter for kNN
        """
        self.folds = self._create_folds(n)
        for i in range(len(self.folds)):
            

        return results

    def _create_folds(self, k):
        """
        Divides given list into k lists of equal (or almost equal if indivisible) number of elements
        :return: list of tuples (feature_class, list of k-lists)
        """

        randomized = random.sample(self.features, len(self.features))
        chunk_size = math.ceil(len(randomized)/k)
        last_chunk_size = len(randomized) - chunk_size * (k-1)
        folds = [randomized[i*chunk_size: (i+1)*chunk_size] for i in range(k-1)]
        folds.append(randomized[-last_chunk_size:])
        try:
            assert sum([len(l) for l in folds]) == len(randomized)
        except AssertionError:
            print("Chunks size don't sum up to length of original list")
            sys.exit()

        return folds
