result = []
for x in range(15):
    if x % 2 == 0:
        result.append(x * x)


 result = [x*x for x in range(15) if x % 2 == 0]
print(result)
