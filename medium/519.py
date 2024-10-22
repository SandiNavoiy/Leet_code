from random import randint


class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n  # Общее количество ячеек
        self.flipped_positions = {}  # Словарь для хранения перевёрнутых позиций
        self.flipped_count = 0  # Счётчик перевёрнутых ячеек

    def flip(self) -> list[int]:
        if self.flipped_count >= self.total:
            return []

        # Генерация случайного индекса в пределах оставшихся позиций
        rand_index = randint(0, self.total - self.flipped_count - 1)

        # Получение фактической позиции для переворота
        actual_position = self.flipped_positions.get(rand_index, rand_index)

        # Обновление словаря перевёрнутых позиций
        self.flipped_positions[rand_index] = self.flipped_positions.get(
            self.total - self.flipped_count - 1, self.total - self.flipped_count - 1
        )

        # Увеличение счётчика перевёрнутых ячеек
        self.flipped_count += 1

        # Преобразование одномерной позиции в двумерные координаты
        return [actual_position // self.n, actual_position % self.n]

    def reset(self) -> None:
        """"""
        self.flipped_positions.clear()
        self.flipped_count = 0


# Your Solution object will be instantiated and called as such:

m = 6
n = 5
obj = Solution(m, n)

param_1 = obj.flip()

# obj.reset()
