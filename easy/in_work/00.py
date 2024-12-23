import os
import time

path = "."
x = os.listdir(path)
file = [i for i in x if os.path.isfile(i)]
dir = [i for i in x if os.path.isdir(i)]

print(file)
print(dir)

for i in file:
    print("File         :", i)
    print("Access time  :", time.ctime(os.path.getatime(i)))
    print("Modified time:", time.ctime(os.path.getmtime(i)))
    print("Change time  :", time.ctime(os.path.getctime(i)))
    print("Size         :", os.path.getsize(i))

for i in dir:
    print("dir         :", i)
    print("Access time  :", time.ctime(os.path.getatime(i)))
    print("Modified time:", time.ctime(os.path.getmtime(i)))
    print("Change time  :", time.ctime(os.path.getctime(i)))
    print("Size         :", os.path.getsize(i))
