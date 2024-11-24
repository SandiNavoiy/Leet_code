from string import ascii_lowercase
x = ascii_lowercase
print(x)
alphabet= {}
ind = 1
for i in x:
    alphabet[i] = ind
    ind += 1

print(alphabet)