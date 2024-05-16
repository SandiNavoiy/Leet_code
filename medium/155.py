class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        else:
            val = min(self.min[-1], val)

            self.min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


val = 5
obj = MinStack()
obj.push(val)
print(obj.stack)
obj.pop()
print(obj.stack)
param_3 = obj.top()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
print(obj.stack)
param_4 = obj.getMin()
print(param_4)
