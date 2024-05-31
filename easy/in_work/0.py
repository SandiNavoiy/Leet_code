array1 = [3, 4, 7, 8]
array2 = [1, 5, 9]


def merge(array1, array2):
    """
    Функция слияния двух отсортированных массивов в один.
    array1 и array2 - массивы представленные python-списками.
    """
    # Добавьте ваш код тут.
    array = []

    arr1 = len(array1)
    arr2 = len(array2)
    i = 0
    j = 0

    while i < arr1 and j < arr2:
        if array1[i] < array2[j]:
            array.append(array1[i])
            i += 1
        else:
            array.append(array2[j])
            j += 1

    if i < arr1:
        array.extend(array1[i:])
    if j < arr2:
        array.extend(array2[j:])
    return array


array = merge(array1, array2)
print(array)
[1, 3, 4, 5, 7, 8, 9]
