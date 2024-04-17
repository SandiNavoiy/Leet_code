class SmallestInfiniteSet:

    def __init__(self):
        self.n = [x for x in range(1, 1001)]

    def popSmallest(self) -> int:
        if len(self.n) > 0:
            return self.n.pop(0)

    def addBack(self, num: int) -> None:
        if num not in self.n:
            self.n.append(num)
            self.n.sort()
num = 5
# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
param_1 = obj.popSmallest()
obj.addBack(num)