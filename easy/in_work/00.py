data = [0, 0, 1, 0, 2, 3]
print(data)


def lstrip(data, param):
    s = []
    Flag = True
    for i in data:
        if i == param and Flag:
            pass
        else:
            s.append(i)
            Flag = False

    return s


print(lstrip(data, 0))
print(data)
