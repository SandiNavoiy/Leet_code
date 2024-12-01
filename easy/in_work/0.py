n = int(input())
matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))


for j in range(len(matr)):
    for i in range(len(matr[j])):
        print(matr[i][j], end=" ")
    print()

