class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size
        self.ritr = 0

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    """
    Двойной стек на базе статического массива.
    """

    def pop_left(self):
        """
        Извлекает элемент из стека слева.
        """
        # Добавьте ваш код тут
        if self.length - 1 < 0:
            return None
        x = self.data[self.length - 1]
        self.data[self.length - 1] = None
        self.length = self.length - 1
        return x

    def pop_right(self):
        """
        Извлекает элемент из стека справа.
        """
        # Добавьте ваш код тут
        if self.ritr < 0:
            return None
        x = self.data[self.size - self.ritr -1]
        self.data[self.size - self.ritr -1] = None
        self.ritr = self.ritr - 1
        return x

    def push_left(self, value):
        """
        Добавляет элемент со значением value в стек слева.
        """
        # Добавьте ваш код тут
        if self.length  + self.ritr < self.size:
            self.data[self.length] = value
            self.length = self.length + 1
        else:
            raise OverflowError

    def push_right(self, value):
        """
        Добавляет элемент со значением value в стек справа.
        """
        # Добавьте ваш код тут
        if self.length  + self.ritr < self.size:
            self.data[self.size - self.ritr -1] = value
            self.ritr = self.ritr + 1
        else:
            raise OverflowError

    def clear(self):
        """
        Очищает стек.
        """
        self.data = [None] * self.size
        self.length = 0

        self.ritr = 0

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        Используем size, так как массив теперь заполняется с двух сторон.
        """
        return "[" + ", ".join(map(str, self.data[:self.size])) + "]"

stack = Stack(6)
stack.push_left(7)
stack.push_left(6)
stack.push_right(2)
stack.push_right(1)
stack.push_left(11)
stack.push_right(8)
print(stack)
print(stack.pop_left())
#11
print(stack.pop_left())
#6
print(stack.pop_left())
#7

print(stack.pop_left())
#2