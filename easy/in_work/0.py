# my_list = input().split()
my_list = [100, 55, 77, 55, 89]

d = {my_list[0]: my_list[0]}
print(d)
for i in my_list[1:]:
    d = d


print(d)
