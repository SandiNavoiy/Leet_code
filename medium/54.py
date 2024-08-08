class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """"""
        rez = []
        while matrix:
            rez.extend(matrix.pop(0))
            matrix = (list(zip(*matrix)))[::-1]

        return rez


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
s = Solution()
print(s.spiralOrder(matrix))
