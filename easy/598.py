class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        min_row = m  # Начальное значение минимального количества строк
        min_col = n  # Начальное значение минимального количества столбцов

        for op in ops:
            min_row = min(min_row, op[0])  # Обновляем минимальное количество строк
            min_col = min(min_col, op[1])  # Обновляем минимальное количество столбцов

        return min_row * min_col  # Возвращаем произведение минимальных количеств строк и столбцов



m = 3
n = 3
ops = [[2, 2], [3, 3]]
s = Solution()
print(s.maxCount(m, n, ops))
