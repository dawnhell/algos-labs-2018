import numpy as np
from random import random, randrange


EXP = 2.7182

class TSPSimulatedAnnealing:
    def __init__(self, array):
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i][j] == -1:
                    array[i][j] = float("inf")

        self.matrix = np.array(array)
        self.graph_size = len(array[0])
        self.path_cost = sum(array[i][i + 1] for i in range(len(array) - 1)) + array[len(array) - 1][0]
        self.path = np.array(range(self.graph_size))

    def solve_koshi(self):
        temperature = 5000
        temperature_max = 5000
        temperature_min = 1
        i = 1

        while temperature > temperature_min:
            new_path, new_cost = self.update_path_2_opt()

            if new_cost < self.path_cost:
                self.path = new_path
                self.path_cost = new_cost
            elif random() <= EXP ** (-(new_cost - self.path_cost) / temperature):
                self.path = new_path
                self.path_cost = new_cost

            temperature = temperature_max / i

            i += 1

        return self.path, self.path_cost

    def solve_bolcman(self):
        temperature = 13
        temperature_max = 13
        temperature_min = 1
        i = 1

        while temperature > temperature_min:
            new_path, new_cost = self.update_path_2_opt()

            if new_cost < self.path_cost:
                self.path = new_path
                self.path_cost = new_cost
            elif random() <= EXP ** (-(new_cost - self.path_cost) / temperature):
                self.path = new_path
                self.path_cost = new_cost

            temperature = temperature_max / np.log2(i + 1)

            i += 1

        return self.path, self.path_cost

    def find_path_cost(self, path):
        cost = 0

        for i in range(self.graph_size - 1):
            cost += self.matrix[path[i], path[i + 1]]

        cost += self.matrix[path[self.graph_size - 1], path[0]]

        return cost

    def update_path_2_opt(self):
        i = randrange(self.graph_size)
        j = randrange(self.graph_size)

        i, j = min(i, j), max(i, j)

        path = np.concatenate((self.path[:i], self.path[i: j][::-1], self.path[j:]))
        cost = self.find_path_cost(path)

        return path, cost

