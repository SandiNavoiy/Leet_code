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

    def push(self, value):
        """
        Добавляет элемент со значением value в стек.
        """
        next_node = Node(value)


stack = Stack()
stack.push(12)
stack.push(7)
stack.push(6)
print(stack.pop())
# 6
print(stack.pop())
# 7
print(stack.pop())
# 12
print(stack.pop())
None
