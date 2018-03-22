import numpy as np


class TSPBranchAndBoundary:
    class Tree:
        def __init__(self, prev, left, right, matrix, vertex, phi, is_taken, vertices):
            self.prev = prev
            self.left = left
            self.right = right
            self.matrix = matrix
            self.vertex = vertex
            self.phi = phi
            self.is_taken = is_taken
            self.vertices = vertices

    def __init__(self, array):
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i][j] == -1:
                    array[i][j] = float("inf")

        self.solution = self.Tree(
            None,
            None,
            None,
            np.array(array),
            None,
            0,
            True,
            [range(len(array)), range(len(array))]
        )

        self.graph_size = len(array[0])
        self.path_cost = sum(array[i][i + 1] for i in range(len(array) - 1)) + array[len(array) - 1][0]
        self.saved_vertex = self.solution
        self.max_fine = 0
        self.max_fine_item = (0, 0)

    def solve(self):
        self.split_plurality(self.solution)

        temp = [-1] * self.graph_size
        while self.saved_vertex.prev:
            if self.saved_vertex.is_taken:
                temp[self.saved_vertex.vertex[0]] = self.saved_vertex.vertex[1]
            self.saved_vertex = self.saved_vertex.prev

        answer = []
        n = 0
        while self.graph_size:
            answer.append(n)
            n = temp[n]
            self.graph_size -= 1

        print (answer, self.path_cost)

    def split_plurality(self, solution):
        if not solution:
            return

        if solution.matrix.shape[0] > 2:
            solution.matrix, solution.phi = self.matrix_reduction(solution.matrix, solution.phi)

            self.zero_fines(solution.matrix)

            vertex_to_go = (solution.vertices[0][self.max_fine_item[0]], solution.vertices[1][self.max_fine_item[1]])

            if not solution.phi + self.max_fine == float("inf") and solution.phi + self.max_fine < self.path_cost:
                temp_matrix = solution.matrix
                if solution.vertex:
                    temp_matrix[solution.vertices[0].index(vertex_to_go[0]), solution.vertices[1].index(vertex_to_go[1])] = float("inf")

                solution.right = self.Tree(
                    solution,
                    None,
                    None,
                    temp_matrix,
                    vertex_to_go,
                    solution.phi + self.max_fine,
                    False,
                    solution.vertices
                )

            solution.matrix = np.delete(solution.matrix, self.max_fine_item[0], 0)
            solution.matrix = np.delete(solution.matrix, self.max_fine_item[1], 1)

            solution.vertices = [
                [x for index, x in enumerate(solution.vertices[0]) if index != self.max_fine_item[0]],
                [x for index, x in enumerate(solution.vertices[1]) if index != self.max_fine_item[1]]
            ]

            solution.matrix = self.prevent_cycles(solution.matrix, vertex_to_go, solution.vertices)
            solution.matrix, solution.phi = self.matrix_reduction(solution.matrix, solution.phi)

            solution.left = self.Tree(
                solution,
                None,
                None,
                solution.matrix,
                vertex_to_go,
                solution.phi,
                True,
                solution.vertices
            )

            self.split_plurality(solution.left)

            self.split_plurality(solution.right)

        if solution.matrix.shape[0] == 2:
            solution.left = self.Tree(
                solution,
                None,
                None,
                solution.matrix,
                (solution.vertices[0][0], solution.vertices[1][np.where(solution.matrix[0, :] != float("inf"))[0][0]]),
                solution.phi + min(solution.matrix[0, :]),
                True,
                solution.vertices
            )
            solution.left.left = self.Tree(
                solution.left,
                None,
                None,
                solution.vertices[1][np.where(solution.matrix[1, :] != float("inf"))[0][0]],
                (solution.vertices[0][1], solution.vertices[1][np.where(solution.matrix[1, :] != float("inf"))[0][0]]),
                solution.phi + min(solution.matrix[1, :]),
                True,
                solution.vertices
            )

            solution = solution.left.left

            if solution.phi < self.path_cost:
                self.path_cost = solution.phi
                self.saved_vertex = solution

    @staticmethod
    def prevent_cycles(matrix, vertex_to_go, vertices):
        if vertex_to_go[1] in vertices[0] and vertex_to_go[0] in vertices[1]:
            matrix[vertices[0].index(vertex_to_go[1]), vertices[1].index(vertex_to_go[0])] = float("inf")
        else:
            row_index = 0
            column_index = 0

            for index, column in enumerate(matrix.transpose()):
                if max(column) < float("inf"):
                    column_index = index
                    break

            for index, row in enumerate(matrix):
                if max(row) < float("inf"):
                    row_index = index
                    break

            matrix[row_index][column_index] = float("inf")

        return matrix

    @staticmethod
    def matrix_reduction(matrix, phi):
        phi += sum(matrix.min(axis=0))
        matrix = matrix - matrix.min(axis=0)
        phi += sum(matrix.min(axis=1))
        matrix = matrix - matrix.min(axis=1)[:, np.newaxis]

        return matrix, phi

    def zero_fines(self, matrix):
        self.max_fine = 0
        self.max_fine_item = (0, 0)

        for row_index, row in enumerate(matrix):
            for index, item in enumerate(row):
                temp_min = 0
                if item == 0:
                    temp = matrix[row_index, index]
                    matrix[row_index, index] = float("inf")
                    temp_min += min(row) + min(matrix[:, index])
                    matrix[row_index, index] = temp

                    if temp_min > self.max_fine:
                        self.max_fine = temp_min
                        self.max_fine_item = (row_index, index)
