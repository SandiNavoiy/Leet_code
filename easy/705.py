class MyHashSet:
    def __init__(self):
        self.new = {}

    def add(self, key: int) -> None:
        self.new[key] = 1

    def remove(self, key: int) -> None:
        self.new[key] = 0

    def contains(self, key: int) -> bool:
        if self.new.get(key) == 1:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
