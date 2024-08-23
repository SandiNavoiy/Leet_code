def quick_power(a, n):
    # Выводим текущее состояние параметров
    print(f"State: a={a}, n={n}")

    # Базовый случай: любое число в нулевой степени равно 1
    if n == 0:
        return 1

    # Если степень n четная
    if n % 2 == 0:
        return quick_power(a, n // 2) ** 2

    # Если степень n нечетная
    else:
        return a * quick_power(a, n - 1)


# Примеры использования
print(quick_power(2, 10))  # Должно вывести 1024
print(quick_power(3, 5))  # Должно вывести 243
