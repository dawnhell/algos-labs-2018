from random import random

NO_EDGE = -1
MAX_VAL = 999999999


def main():
    arr, n = read_array()
    print n, arr
    print tsp_brute_force(arr, n)


def generate_graph(n, max_val):
    return [[int(random() * max_val + 1) if i != j else NO_EDGE for j in range(n)] for i in range(n)]


def read_array():
    input_file = open("TSP.txt", "r")
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


def tsp_brute_force(array, n):
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
