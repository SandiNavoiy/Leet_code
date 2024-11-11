def dec(f):
    def wrapper(x):
        return f(x) + 5

    return wrapper


@dec
def square(x):
    return x


print(square(10))
