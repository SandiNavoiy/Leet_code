class MapSum:
    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        s = 0
        for key, val in self.map.items():
            if prefix == key[0 : len(prefix)]:
                s = s + val
        return s


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
key = "aw"
val = 3
obj.insert(key, val)
print(obj.map)
key = "wtt"
val = 44
obj.insert(key, val)
print(obj.map)
prefix = "aw"
param_2 = obj.sum(prefix)
print(param_2)
