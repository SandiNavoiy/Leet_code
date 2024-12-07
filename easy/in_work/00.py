def coroutine():
    a = yield 10
    b = yield
    yield a + b

coro = coroutine()
value = next(coro)
print(value)
# coro.send(23)
# result = coro.send(value)
# print(result)