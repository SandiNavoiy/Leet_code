class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = []
        self.size = k

    def enQueue(self, value: int) -> bool:
        """вставка элемена"""
        if len(self.queue) == self.size:
            return False
        self.queue.append(value)
        return True

    def deQueue(self) -> bool:
        """Удаление элемента"""
        if len(self.queue) == 0:
            return False
        self.queue.pop(0)
        return True

    def Front(self) -> int:
        """вывод первого элемента"""
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        """последний элемент"""
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        """проверка на пустоту"""
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self) -> bool:
        """Заполненость"""
        if len(self.queue) == self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
k = 100
obj = MyCircularQueue(k)
value = 5
param_1 = obj.enQueue(value)
value = 6
param_1 = obj.enQueue(value)
print(obj.queue)
param_2 = obj.deQueue()
print(param_2)
param_3 = obj.Front()
print(param_3)
param_4 = obj.Rear()
print(param_4)
param_5 = obj.isEmpty()
print(param_5)
param_6 = obj.isFull()
print(param_6)
