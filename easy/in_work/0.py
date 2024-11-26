s = []
for i in range (1000, 10000):
    temp = 0
    for j in str(i):
        temp +=int(j)
    if temp == 20:
        s.append(i)
print(sum(s))



