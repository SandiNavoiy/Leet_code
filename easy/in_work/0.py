# n, = input()
# s1 = list(map(int, input().split()))
# m = input()
# s2 = list(map(int, input().split()))
s1 = [6,4,2,1]
s2 = [9,7,5,5,1]
s1.sort(reverse=True)
s2.sort(reverse=True)
count= 0
while len(s1) > 0 and len(s2) > 0:
    if (abs(s1[0] - s2[0]) <= 1) or (abs(s2[0] - s1[0]) <= 1):
        s1.pop(0)
        s2.pop(0)
        count += 1
        print("первая ветка")
    else:
        print("вторая ветка")
        if s1[0] > s2[0]:
            s1.pop(0)
        else:
            s2.pop(0)

    print(s1, s2, count)

print(count)