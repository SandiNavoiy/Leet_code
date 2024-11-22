n = input().split()
s = []
temp = []
for i in range(len(n)):
    if n[i].lower() not in temp:
        temp.append(n[i].lower())
        s.append(n[i])
print(*s)
