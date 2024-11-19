x = int(input())

while x <= 1000000000:
    x = x * int(str(x)[0])

    if str(x)[0] == "1":
        break
print(x)
