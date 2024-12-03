x = "chase enlarge referee cup offense".lower()

for i in x.split():
    print(i)
print(all([True if "a" in i else False for i in x.split()]))
