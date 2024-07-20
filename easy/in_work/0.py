# Получаем значение, которое будем искать
val = int(input())

# Получаем список элементов, в которых будем искать
values = list(map(int, input().split()))


# Запуск функции с выводом ответа
def search(arr, val):
    minn = 0
    maxx = len(arr) - 1
    result = -1
    while minn <= maxx:
        mid = (maxx + minn) // 2
        if val < arr[mid]:
            maxx = mid - 1
        elif val > arr[mid]:
            minn = mid + 1
        else:
            result = mid
            minn = mid + 1

    return result


print(search(values, val))
