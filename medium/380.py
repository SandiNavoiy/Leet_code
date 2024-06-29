import random


class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.ind = 0

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data[val] = self.ind
        self.ind = self.ind + 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        del self.data[val]
        self.ind = self.ind - 1
        return True

    def getRandom(self) -> int:
        t = list(self.data.keys())

        return random.choice(t)

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
val = 1
param_1 = obj.insert(val)
val = 2
param_1 = obj.insert(val)
print(param_1)
val = 3
param_1 = obj.insert(val)
print(obj.data)

param_2 = obj.remove(val)
print(obj.data)
param_3 = obj.getRandom()
print(param_3)