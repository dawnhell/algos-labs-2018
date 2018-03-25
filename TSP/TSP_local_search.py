import numpy as np


class TSPLocalSearch:
    def __init__(self, array):
        self.matrix = np.array(array)
        self.graph_size = len(array[0]) - 1
        self.path = np.arange(self.graph_size + 1)
        self.path_cost = sum(array[i][i + 1] for i in range(self.graph_size)) + array[self.graph_size][0]

    def solve_2_opt(self):
        can_update = self.can_update_2_opt()

        while can_update and self.path_cost > 0:
            can_update = self.can_update_2_opt()

        return self.path, self.path_cost

    def solve_3_opt(self):
        can_update = self.can_update_3_opt()

        while can_update and self.path_cost > 0:
            can_update = self.can_update_3_opt()

        return self.path, self.path_cost

    def find_path_cost(self, path):
        cost = 0

        for i, _ in enumerate(path):
            if i < self.graph_size:
                cost += self.matrix[path[i], path[i + 1]]

        cost += self.matrix[path[self.graph_size], path[0]]

        return cost

    def can_update_2_opt(self):
        for index, item in enumerate(self.path):
            for j in range(2, self.graph_size - 2):
                ia = index + 1
                ib = index + j + 1

                new_path = self.path

                if ib > self.graph_size:
                    diff = ib - self.graph_size

                    new_path = np.roll(new_path, -diff)
                    ia -= diff
                    ib -= diff

                new_path = np.concatenate((new_path[:ia], np.array(list(reversed(new_path[ia:ib]))), new_path[ib:]))

                new_path_cost = self.find_path_cost(map(int, new_path))

                if new_path_cost < self.path_cost:
                    self.path = new_path
                    self.path_cost = new_path_cost
                    return True

        return False

    def can_update_3_opt(self):
        for index, item in enumerate(self.path):
            for j in range(1, self.graph_size):
                if abs(j - index) > 1:
                    new_path = self.path
                    new_path = np.delete(new_path, index, 0)

                    new_path = np.insert(new_path, j, item)
                    new_cost = self.find_path_cost(new_path)

                    if new_cost < self.path_cost:
                        self.path_cost = new_cost
                        self.path = new_path
                        return True

        return False
