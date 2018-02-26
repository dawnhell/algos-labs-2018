def main():
    file = open("Independent_set(road_graph).txt", "r")
    array = map(int, file.readline().split())

    print array

    d = list()
    path = list()

    path.append(0)
    path.append(0 if (array[0] > array[1]) else 1)
    d.append(0)
    d.append(array[0])
    d.append(max(array[0], array[1]))

    for i in range(2, len(array)):
        d.append(max(d[i - 1] + array[i], d[i]))

        if d[i - 1] + array[i] > d[i]:
            path.append(i)

    print d[len(d) - 1]

    for i in range(len(path) - 1, 0, -1):
        if path[i] - path[i - 1] < 2:
            path.pop(i - 1)

    print path


main()
