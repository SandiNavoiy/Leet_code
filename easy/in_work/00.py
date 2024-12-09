def flatten(lst):
    # проверяем, не пустой ли список.
    for i in lst:
        if isinstance(i, list):
            yield  from flatten(i)
        else:
            yield i


for element in flatten([1, [2], [3, [4]]]):
    print(element)