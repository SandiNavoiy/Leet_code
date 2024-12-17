from collections import Counter


def find_difference_with_counter(lst1: list, lst2: list) -> list:
    c1 = Counter(lst1)
    c2 = Counter(lst2)
    rez = []
    for i in c1 - c2:
        rez.append(i)
    rez.sort()
    return rez


print(find_difference_with_counter([1, 1, 2, 3, 3, 4, 4, 5, 6, 7], [1, 1, 2, 4, 5, 6]))
assert find_difference_with_counter([1, 2, 2, 3, 4, 4, 5], [2, 3, 3, 4, 5, 6]) == [
    1,
    2,
    4,
]
#
assert find_difference_with_counter([5, 4, 5, 1, 2, 7, 3], [2, 3, 3, 4, 5, 6]) == [
    1,
    5,
    7,
]

assert find_difference_with_counter(
    [1, 1, 2, 3, 3, 4, 4, 5, 6, 7], [1, 1, 2, 4, 5, 6]
) == [3, 3, 4, 7]

# assert find_difference_with_counter(
#     [1, 1, 1, 1],
#     [
#         1,
#         1,
#     ],
# ) == [1, 1]

# assert (
#     find_difference_with_counter(
#         [
#             1,
#             1,
#         ],
#         [1, 1, 1, 1],
#     )
#     == []
# )
