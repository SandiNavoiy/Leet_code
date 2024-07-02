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

    def __init__(self, size):
        self.top = Node(None)
        self.first = None
        self.size = size
        self.count_nodes = 0  # Счетчик элементов в очереди

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        new_node = Node(value)
        if self.count_nodes >= self.size:
            raise OverflowError("Очередь переполнена")

        # Вставялем элемент в начало.

        # Связываем последний элемент в очереди с новым.
        if self.top.next_node:
            self.top.next_node.prev_node = new_node

        # Связываем новый элемент со следующим (последним) и с top.
        new_node.next_node = self.top.next_node
        new_node.prev_node = self.top

        # Связываем top с новым.
        self.top.next_node = new_node

        # Устанавливаем first, если это первая вставка.
        if not self.first:
            self.first = new_node

        self.count_nodes += 1  # Увеличиваем счетчик элементов

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """

        # Если элемент есть, то получаем его значение.
        if self.first:
            value = self.first.value

            # Смещаем указатель.
            self.first = self.first.prev_node

            # Удаляем последний элемент.
            if self.first:
                self.first.next_node = None

            # Проверяем, не ссылается ли first на top.
            # Если ссылается, то сбрасываем first.
            if self.first == self.top:
                self.first = None

            self.count_nodes -= 1  # Уменьшаем счетчик элементов

            return value

        return None

    def count(self):
        """
        Возвращает количество элементов в очереди.
        """
        return self.count_nodes

    def peek(self):
        """
        Возвращает значение первого элемента очереди без его извлечения.
        """
        if self.first:
            return self.first.value
        return None

    def clear(self):
        """
        Очищает очередь.
        """
        self.top.next_node = None
        self.first = None
        self.count_nodes = 0


queue = Queue(3)
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(6)
...
# OverflowError
print(queue.dequeue())
12
print(queue.count())
2
queue.clear()
print(queue.count())
0
print(queue.peek())
None
