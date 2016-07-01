class AGDSHelpers(object):
    def __init__(self, agds):
        self.agds = agds

    def filter_single_param(self, param, range_min, range_max):
        param_tree = self.agds.root.get(param).connections
        vals = param_tree.keys()
        found_vals = list(filter(lambda x: range_min <= x <= range_max, vals))
        found = set()
        for val in found_vals:
            found |= set(param_tree[val].connections.keys())
        return found

    def filter_multi_param(self, params):
        """
        :param params: list of tuples ('param_name', range_min, range_max)
        """
        param, range_min, range_max = params.pop(0)
        result = self.filter_single_param(param, range_min, range_max)
        for param, range_min, range_max in params:
            result |= self.filter_single_param(param, range_min, range_max)
        return result
