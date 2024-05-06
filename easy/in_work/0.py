def linear_search(arr, target):
    n = len(arr)
    rez = []

    for i in range(n):
        if arr[i] == target:
            rez.append(i)

    if len(rez) == 0:
        return -1
    return rez


idx = linear_search([1, 3, 3, 4], 3)
print(idx)
[1, 2]
