from random import random

NO_EDGE = -1


def main():
    arr, n = read_array()
    print n, arr
    find_cycle(arr, n)


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



main()
