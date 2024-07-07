def bubblesort(array):
    """
    Алгоритм пузырьковой сортировки массива в прямом порядке.
    """

    # Модифицируйте алгоритм.
    n = 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True

        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        n += 1
    return array


print(bubblesort([1,5,9,7,2,7,0,4,3]))