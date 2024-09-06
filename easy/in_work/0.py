import functools


def counting_calls(func):
    func.call_count = 0  # Инициализация счетчика вызовов
    func.calls = []  # Инициализация списка для хранения переданных аргументов

    @functools.wraps(func)  # Сохраняет метаданные оригинальной функции
    def wrapper(*args, **kwargs):
        # Увеличиваем счетчик вызовов
        wrapper.call_count += 1

        # Сохраняем аргументы в виде словаря
        wrapper.calls.append({"args": args, "kwargs": kwargs})

        # Вызываем оригинальную функцию и возвращаем результат
        return func(*args, **kwargs)

    # Передаем атрибуты в обертку, а не в оригинальную функцию
    wrapper.call_count = func.call_count
    wrapper.calls = func.calls

    return wrapper


@counting_calls
def add(a: int, b: int) -> int:
    """Возвращает сумму двух чисел"""
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print("Количество вызовов =", add.call_count)
print(add.calls)

print(add(5, 6))
print(add.calls[1])
