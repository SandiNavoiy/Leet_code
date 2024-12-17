from collections import defaultdict

sales = [('Clothing', 5.0),
         ('Clothing', 6.0),
         ('Outdoor', 7.0),
         ('Grocery', 2.0),
         ('Grocery', 3.0),
         ('Grocery', 2.0)]

d= defaultdict(int)
for i in sales:
    d[i[0]] += i[1]
name = ""
col = 0
for i, v in d.items():
    if v > col:
        col = v
        name = i
print(f"{name} - {col}")