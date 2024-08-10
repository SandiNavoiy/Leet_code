def summa(param):
    if param == 1:
        return param
    else:
        return param + summa(param - 1)


print(summa(4))
