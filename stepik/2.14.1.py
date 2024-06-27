class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return self.value


class Queue:
    """
    Очередь на базе двунаправленного связного списка.
    """

    def __init__(self):
        self.top = Node(None)

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        cur = self.top
        if cur.next_node is None:
            cur = Node(value)
            self.top.next_node = cur
            cur.prev_node = self.top
            return
        while cur.next_node is not None:
            cur = cur.next_node
        cur = Node(value)
        self.top.next_node = cur
        cur.prev_node = self.top

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        # Добавьте ваш код тут


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
