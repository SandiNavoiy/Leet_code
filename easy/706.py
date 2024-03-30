class MyHashMap:

    def __init__(self):
        self.d = {}

    def put(self, key: int, value: int) -> None:
        self.d[key] = value

    def get(self, key: int) -> int:
        v= self.d.get(key)
        return v if v != None else -1

    def remove(self, key: int) -> None:
        self.data[key]=None
key = 1
value = 2
# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(key,value)
print(obj.d)
param_2 = obj.get(key)
print(param_2)
obj.remove(key)