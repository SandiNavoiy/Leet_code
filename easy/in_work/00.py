import itertools

x = 17
y = 32684323
rez = [chr(i + 64) for i in range(1, x+1)]
count = 1
for i in itertools.permutations(rez):
    if count == y:
        print(' '.join(map(str, i)))
        break
    count = count + 1