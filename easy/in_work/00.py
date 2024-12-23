import os
from datetime import time


import os
import time

path = "."
files_lst = os.listdir(path)
print(files_lst)
idxs = list()

for idx in range(len(files_lst)):
    print(idx)
    name = os.path.split(files_lst[idx])[1]

    if os.path.isfile(os.path.join(path, name)):
        idxs.append(idx)

print(idxs)
for indx in range(len(idxs)):
    print("File         :", files_lst[indx])
    print("Access time  :", time.ctime(os.path.getatime(files_lst[indx])))
    print("Modified time:", time.ctime(os.path.getmtime(files_lst[indx])))
    print("Change time  :", time.ctime(os.path.getctime(files_lst[indx])))
    print("Size         :", os.path.getsize(files_lst[indx]))
    if indx == len(idxs) - 1:
        break
    print("---------------------------------------")
