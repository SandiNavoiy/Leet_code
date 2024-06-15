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


class Stack(Array):
    """
    Стек на базе статического массива.
    """

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        # Добавьте ваш код тут

        x = self.data[self.length - 1]
        self.data[self.length - 1] = None
        self.length = self.length - 1
        return x

    def push(self, value):
        """
        Добавялет элемент со значением value в стек.
        """
        # Добавьте ваш код тут
        if self.length < self.size:
            self.data[self.length] = value
            self.length = self.length + 1
        else:
            raise OverflowError
