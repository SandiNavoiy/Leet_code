class MyQueue:
    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        return self.arr.pop(0)

    def peek(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        if len(self.arr) == 0:
            return True
        return False


x = 2
# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(x)
print(obj.arr)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
