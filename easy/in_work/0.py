def reversed_recursive(lst):
    t = []
    for i in lst:
        if isinstance(i, list):
            t.append(reversed_recursive(i))
        else:
            t.append(i)

    return list(reversed(t))


print(reversed_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
