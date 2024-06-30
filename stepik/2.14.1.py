class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return str(self.value)


class Queue:
    """
    Очередь на базе двунаправленного связного списка.
    """

    def __init__(self):
        self.top = None
        self.tail = None

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        new_node = Node(value)
        if self.tail is None:  # Если очередь пуста
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        if self.top is None:  # Если очередь пуста
            return None
        dequeued_value = self.top.value
        self.top = self.top.next_node
        if self.top is not None:
            self.top.prev_node = None
        else:
            self.tail = None
        return dequeued_value


queue = Queue()
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(8)
print(queue.dequeue())
12
print(queue.dequeue())
7
print(queue.dequeue())
6
print(queue.dequeue())
8
print(queue.dequeue())
None
