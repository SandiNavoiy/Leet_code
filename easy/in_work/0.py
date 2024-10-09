def get_average():
    total = 0
    count = 0
    while True:
        number = (
            yield total / count if count > 0 else 0
        )  # Возвращаем среднее, если есть числа
        total += number
        count += 1


coro = get_average()
next(coro)
print(coro.send(10))
print(coro.send(20))
print(coro.send(6))
