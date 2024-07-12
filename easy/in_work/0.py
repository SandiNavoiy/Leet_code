def double_it(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return wrapper


def increment(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 1

    return wrapper


def add(num1, num2):
    return num1 + num2


add = double_it(increment(add))

print(add(5, 7))