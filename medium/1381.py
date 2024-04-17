class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.m = []

    def push(self, x: int) -> None:
        if len(self.m) < self.maxSize:
            self.m.append(x)

    def pop(self) -> int:
        if len(self.m) > 0:
            return self.m.pop(-1)
        return -1

    def increment(self, k: int, val: int) -> None:
        if k <= len(self.m):
            for i in range(0,k):
                self.m[i] = self.m[i] + val
        else:
            for i in range(0,len(self.m)):
                self.m[i] = self.m[i] + val
maxSize = 3
# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)