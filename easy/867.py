import numpy as np


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """"""

        new = np.transpose(matrix)
        return new


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.transpose(matrix))
