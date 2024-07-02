class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[: self.length])) + "]"


class Queue(Array):
    """
    Очередь на базе статического массива.
    """

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        if self.length == self.size:
            raise OverflowError("Очередь переполнена")
        self.data[self.length] = value
        self.length += 1

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        if self.length == 0:
            return None
        x = self.data.pop(0)
        self.length -= 1
        self.data.append(None)
        return x


queue = Queue(4)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(2)
queue.enqueue(1)
print(queue.data)
...
# OverflowError
print(queue.dequeue())
12
print(queue.dequeue())
7
print(queue.dequeue())
6
print(queue.dequeue())
None
