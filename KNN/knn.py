import random
import math
import sys
import itertools


class KNN(object):
    def __init__(self, features):
        self.features = features
        self.folds = None

    def knn(self, validation_features, test_features):
        pass

    def cross_validate(self, k=3):
        """
        Test set using k-fold cross validation
        :param k: how many folds to create
        """
        self.folds = self._create_folds(k)
        combs = itertools.combinations(self.folds, k)
        results = [self.knn(comb[0], comb[1:]) for comb in combs]
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
