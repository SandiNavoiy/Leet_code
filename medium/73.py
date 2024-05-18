import numpy as np


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        np_matrix = np.array(matrix)

        # Находим индексы строк и столбцов, содержащих нули
        rows_with_zeros = np.any(np_matrix == 0, axis=1)
        cols_with_zeros = np.any(np_matrix == 0, axis=0)

        # Заполняем нулями соответствующие строки и столбцы
        np_matrix[rows_with_zeros, :] = 0
        np_matrix[:, cols_with_zeros] = 0
        matrix = np_matrix.tolist()

        return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
s = Solution()
print(s.setZeroes(matrix))
