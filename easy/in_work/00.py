from collections import deque

# q = deque(list(map(int, input().split())))

q = deque([3, 7, 2, 5, 9])

fist = 0
second = 0
while len(q) > 0:
    fist += q.popleft()
    if len(q) > 0:
        second += q.pop()
if fist > second:
    print("FIRST")
elif fist < second:
    print("SECOND")

else:
    print("DRAW")
