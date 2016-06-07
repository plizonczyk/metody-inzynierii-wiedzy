import sys


class Feature(object):
    def __init__(self, data_dict, class_fieldname):
        self.data_dict = data_dict
        self.feature_class = self.data_dict.pop(class_fieldname)
        self.values = self._prepare_values()

    def __repr__(self):
        return 'Feature class "{feature_class}": features: {features}'.format(
            feature_class=self.feature_class, features=' '.join(map(str, self.values)))

    def _prepare_values(self):
        try:
            return [float(val) for val in self.data_dict.values()]
        except ValueError:
            print("Invalid data format - failed on float conversion")
            sys.exit()
