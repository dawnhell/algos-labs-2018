from random import random
import time

from TSP_branch_and_boundary import TSPBranchAndBoundary
from TSP_local_search import TSPLocalSearch

NO_EDGE = -1
MAX_VAL = 999999999


def main():
    arr, n = read_array()
    print n, "\n", arr, "\n"

    print "Brute force:"
    start_time = time.time()
    print tsp_brute_force(arr, n)
    tsp_brute_force_time = time.time() - start_time
    print tsp_brute_force_time, "\n"

    print "Greedy:"
    start_time = time.time()
    print tsp_greedy(arr, n)
    tsp_greedy_time = time.time() - start_time
    print tsp_greedy_time, "\n"

    print "Branch and boundary:"
    start_time = time.time()
    TSPBranchAndBoundary(arr).solve()
    tsp_branch_and_boundary_time = time.time() - start_time
    print tsp_branch_and_boundary_time, "\n"

    print "Local search(2 substitution):"
    start_time = time.time()
    print TSPLocalSearch(arr).solve_2_substitution()
    tsp_local_search_2_time = time.time() - start_time
    print tsp_local_search_2_time, "\n"


def generate_graph(n, max_val):
    return [[int(random() * max_val + 1) if i != j else NO_EDGE for j in range(n)] for i in range(n)]


def read_array():
    input_file = open("TSP/TSP.txt", "r")
    n = int(input_file.readline())
    arr = []

    for _ in range(n):
        arr.append([int(x) for x in input_file.readline().split()])

    return arr, n


def dfs(array, vertex, colors, is_cyclic):
    colors[vertex] = 1

    for i, item in enumerate(array[vertex]):
        if i != vertex and item != NO_EDGE:
            if colors[i] == 0:
                if dfs(array, i, colors, is_cyclic):
                    return True
            elif colors[i] == 1:
                return True

    colors[vertex] = 2

    return False


def find_cycle(array, n):
    colors = [0] * n
    is_cyclic = False

    for i in range(n):
        if dfs(array, i, colors, is_cyclic):
            is_cyclic = True
            break

    if is_cyclic:
        print "Cyclic"
    else:
        print "Acyclic"


def generate_permutations(array, low=0):
    if low + 1 >= len(array):
        yield array
    else:
        for p in generate_permutations(array, low + 1):
            yield p
        for i in range(low + 1, len(array)):
            array[low], array[i] = array[i], array[low]
            for p in generate_permutations(array, low + 1):
                yield p
            array[low], array[i] = array[i], array[low]


def tsp_brute_force(array, n):
    path_cost = MAX_VAL
    path = []

    for permutation in generate_permutations(range(n), 1):
        length = len(permutation)
        temp_cost = 0

        for i in range(length - 1):
            temp_cost += array[permutation[i]][permutation[i + 1]]

        temp_cost += array[permutation[length - 1]][0]

        if temp_cost < path_cost:
            path = list(permutation)
            path_cost = temp_cost

    return path, path_cost


def tsp_greedy(array, n):
    path = [0]
    path_cost = 0
    prev_index = 0

    for i in range(n):
        min_val = MAX_VAL
        min_index = 0

        for j, item in enumerate(array[prev_index]):
            if prev_index != j and item < min_val:
                if i == n - 1:
                    min_val = item
                    min_index = j
                elif j not in path:
                    min_val = item
                    min_index = j

        prev_index = min_index
        path.append(min_index)
        path_cost += min_val

    return path, path_cost


main()
