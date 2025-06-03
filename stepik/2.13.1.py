class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class Stack:
    def __init__(self):
        self.top = Node(None)

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        # Добавьте ваш код тут.
        if self.top is None:
            return None
        val = self.top.value
        self.top = self.top.next_node
        return val

    def push(self, value):
        """
        Добавляет элемент со значением value в стек.
        """
        next_node = Node(value)
        next_node.next_node = self.top
        self.top = next_node


# ckvkjkf
