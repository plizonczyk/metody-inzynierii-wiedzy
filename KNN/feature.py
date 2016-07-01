import sys
import itertools

import math


class Feature(object):
    cnt = itertools.count(0)

    def __init__(self, data_dict, class_fieldname):
        self.data_dict = data_dict
        self.feature_class = self.data_dict.pop(class_fieldname)
        self.values = self._prepare_values()
        self.feature_id = next(self.cnt)

    def __repr__(self):
        return 'Feature id {id}, class "{feature_class}", features: {features}'.format(
            id=self.feature_id, feature_class=self.feature_class, features=' '.join(map(str, self.values)))

    def _prepare_values(self):
        try:
            for key in self.data_dict:
                self.data_dict[key] = float(self.data_dict[key])
        except ValueError:
            print("Invalid data format - failed on float conversion")
            sys.exit()
        return self.data_dict.values()

    def euclidean_to_values(self, values_dict):
        sum = 0
        for key, value in values_dict.items():
            sum += (self.data_dict[key] - value)**2
        return math.sqrt(sum)
