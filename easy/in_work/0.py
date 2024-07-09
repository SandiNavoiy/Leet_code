lines = [(5, 6), (5, 4), (1, 0), (0, -1), (1, 2), (2, 1)]


def get_sort_lines(l):
    l = sorted(l, key=lambda x: (abs(x[1] - x[0]), x[0], x[1]))
    return l


print(get_sort_lines(lines))
# [(-1, -2), (1, 0), (2, 3), (5, 4)]
