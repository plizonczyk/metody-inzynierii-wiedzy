import random
import math
import sys
import itertools
import collections


class KNN(object):
    def __init__(self, features):
        self.features = features
        self.folds = None
        self.distance_method = self._euclidean

    def knn(self, validation_set, training_set, k=3):
        results = []
        for feature in validation_set:
            # create list of tuples in format (distance, referenced feature's class) then sort it
            distances = [(self.distance_method(feature.values, training_feature.values), training_feature.feature_class)
                         for training_feature in training_set]
            distances.sort(key=lambda x: x[0])

            # pick k lowest distances then extract feature classes and pick the most common one (arbitrary if equal)
            distances = [x[1] for x in distances[0:k]]
            most_common_class = collections.Counter(distances).most_common(1)[0][0]
            results.append((feature, most_common_class))
        return results

    def cross_validate(self, n=3, k=3):
        """
        Test set using n-fold cross validation with kNN method
        :param method: method to use (knn or weighted_knn)
        :param n: how many folds to create
        :param k: parameter for kNN
        """
        self.folds = self._create_folds(n)
        full_results = []
        accuracies = []
        for validation_set in self.folds:
            # exclude validation set from training sets
            training_set = list(itertools.chain(*[x for x in self.folds if x != validation_set]))
            results = self.knn(validation_set, training_set, k)
            full_results.append(results)

            accurate_hits = sum(1 if x[0].feature_class == x[1] else 0 for x in results)
            accuracies.append(accurate_hits / len(results))

        overall_accuracy = sum(accuracies) / len(accuracies)
        return overall_accuracy, full_results

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

    def _euclidean(self, x, y):
        distance = 0
        for val1, val2 in zip(x, y):
            distance += (val1 - val2)**2
        return math.sqrt(distance)
