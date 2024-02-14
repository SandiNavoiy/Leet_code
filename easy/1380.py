class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        """"""
        ss = 0
        for i in range(len(matrix)):
            matrix[i].sort()
            if matrix[i][0] > ss:
                ss = matrix[i][0]
        return ss


matrix = [[-5, 0], [0, 0]]
s = Solution()
print(s.luckyNumbers(matrix))
