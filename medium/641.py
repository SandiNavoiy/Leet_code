from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque()
        self.size = k

    def insertFront(self, value: int) -> bool:
        '''добавление елемента в начало'''
        if self.size == len(self.queue):
            return False
        self.queue.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        '''добавление элемента в конец'''
        if self.size == len(self.queue):
            return False
        self.queue.append(value)
        return True

    def deleteFront(self) -> bool:
        '''удаляет с начала'''
        if  len(self.queue) == 0:
            return False
        self.queue.popleft()
        return True

    def deleteLast(self) -> bool:
        '''удаление с конца'''
        if  len(self.queue) == 0:
            return False
        self.queue.pop()
        return True

    def getFront(self) -> int:
        '''возвращает левый элемент'''
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def getRear(self) -> int:
        '''возвращает правый элемент'''
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        '''пустой'''
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self) -> bool:
        '''полный'''
        if len(self.queue) == self.size:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
k = 5
obj = MyCircularDeque(k)
value = 2
param_1 = obj.insertFront(value)
value = 3
param_2 = obj.insertLast(value)
print(obj.queue)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
print(obj.queue)
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()