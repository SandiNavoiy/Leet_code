count = 1


def gen_arithmetic_progression(param, param1):
    while True:
        yield param
        param = param + param1



for value in gen_arithmetic_progression(5, 7):
    print(value)
    count += 1
    if count > 5:
        break