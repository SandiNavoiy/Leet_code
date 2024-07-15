def limit_query(param):

    def dec(f):
        limit = 0
        def wrapper(*args, **kwargs):
            if limit <= 3:
                limit = limit + 1
                return f(*args, **kwargs)
        return wrapper
    return dec



@limit_query(3)
def add(a: int, b: int):
    return a + b

print(add(4, 5))
print(add(5, 8))
print(add(9, 43))
print(add(10, 33))
print(add.__name__)