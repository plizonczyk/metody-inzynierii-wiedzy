import random
import math


class SOM(object):
    def __init__(self, param_names, params_dict):
        self.param_names = param_names
        self.size = params_dict['matrix_size']
        self.initial_sigma = params_dict['initial_sigma']
        self.initial_gamma = params_dict['initial_gamma']
        self.alpha = params_dict['alpha']
        self.matrix = [[Neuron(param_names) for _ in range(self.size)] for __ in range(self.size)]
        self.sigma = 0
        self.gamma = 0
        self.time = 0
        self.results = []

    def delta(self, winner, neuron):
        return math.exp(-(self.euclidean(winner, neuron)**2)/(2*self.sigma**2))

    def recalculate_sigma(self):
        self.sigma = self.initial_sigma * math.exp(-self.time/self.alpha)

    def recalculate_gamma(self):
        self.gamma = self.initial_gamma * math.exp(-self.time/self.alpha)

    @staticmethod
    def euclidean(first, second):
        return math.sqrt((first[0]-second[0])**2 + (first[1]-second[1])**2)

    def find_winner(self, feature):
        winner = (0, 0)
        winner_distance = math.inf
        for i in range(self.size):
            for j in range(self.size):
                dist = feature.euclidean_to_values(self.matrix[i][j].dict)
                if dist < winner_distance:
                    winner_distance = dist
                    winner = (i, j)
        return winner, winner_distance

    def update_weights(self, winner, feature):
        new_matrix = [[Neuron(self.param_names) for _ in range(self.size)] for __ in range(self.size)]

        # calculate the range to change
        x_min = math.ceil(winner[0] - self.sigma) if winner[0] - self.sigma > 0 else 0
        y_min = math.ceil(winner[1] - self.sigma) if winner[1] - self.sigma > 0 else 0
        x_max = math.floor(winner[0] + self.sigma) if winner[0] + self.sigma < self.size else self.size-1
        y_max = math.floor(winner[1] + self.sigma) if winner[1] + self.sigma < self.size else self.size-1
        # print(x_min, winner[0], x_max, y_min, winner[1], y_max)

        for i in range(self.size):
            for j in range(self.size):
                for param in self.param_names:
                    new_matrix[i][j].dict[param] = self.matrix[i][j].dict[param]
                    if x_min <= i <= x_max and y_min <= j <= y_max:
                        new_matrix[i][j].dict[param] += self.delta(winner, (i, j)) * self.gamma * \
                                                       (feature.data_dict[param] - self.matrix[i][j].dict[param])

        self.matrix = new_matrix

    def teach(self, feature):
        self.recalculate_gamma()
        self.recalculate_sigma()
        winner, dist = self.find_winner(feature)
        self.update_weights(winner, feature)
        print('Feature', feature, 'Pass finished at time', self.time, 'calculated sigma', self.sigma,
              'gamma', self.gamma, 'winner', winner, 'with distance', dist)
        self.results.append((self.time, feature.feature_class, winner, dist))
        self.time += 1


class Neuron(object):
    def __init__(self, param_names):
        self.dict = {k: random.random()*10 for k in param_names}

    def __repr__(self):
        return "Neuron " + str(self.dict)
