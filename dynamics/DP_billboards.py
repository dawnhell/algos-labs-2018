def main():
    file = open("DP_billboards.txt", "r")

    n = int(file.readline())
    x_array = map(int, file.readline().split())
    r_array = map(int, file.readline().split())
    file.close()

    print n
    print x_array
    print r_array

    find_optimal(n, x_array, r_array)


def find_optimal(n, x_array, r_array):
    d = list()
    path = list()

    path.append(0)
    d.append(0)
    d.append(r_array[0])

    for i in range(1, n):
        index = get_optimal_point(x_array, i)
        d.append(max(r_array[i] + d[index], d[i]))

        if r_array[i] + d[index] > d[i]:
            path.append(i)

    print d[len(d) - 1]
    print_answer(path, x_array)


def get_optimal_point(array, i):
    index = 0

    while array[i] - array[index] > 5:
        index += 1

    return index


def print_answer(path, array):
    for i in range(len(path) - 1, 1, -1):
        if array[path[i]] - array[path[i - 1]] < 6:
            path.pop(i - 1)

    if path[0] == 0:
        path.pop(0)

    print path


main()
