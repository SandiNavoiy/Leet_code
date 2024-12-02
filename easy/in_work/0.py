n,m=map(int,input().split())

a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
#
#
# a = [[5,9,2,6], [6,2,4,3], [1,2,8,7]]


for i in a:
    print(sum(i), end = " ")
print()
for j in range(len(a[0])):
    s = 0
    for i in range(len(a)):

            s = s + a[i][j]
    print(s, end = " ")
