class Array:
    """
    Линейный ститический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполнненого массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        if self.length == self.size:
            raise OverflowError
        self.data[self.length] = value
        self.length += 1

    def insert(self, index, value):
        """
        Добавление нового элемента со значением value на позицию index.
        """
        # Добавьте ваш код тут.
        if self.length == self.size:
            raise OverflowError
        elif index > self.size and self.length < self.size:
            self.data[self.length] = value
            self.length += 1
        elif index > self.length and index < self.size:
            self.data[self.length] = value
            self.length += 1

        elif self.length < self.size:
            self.data.insert(index, value)
            self.length += 1
            self.data.pop()


def __str__(self):
    """
    Возвращает все элементы массива в виде строки.
    """
    return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


