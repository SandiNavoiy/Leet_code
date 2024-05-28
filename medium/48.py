class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) // 2):
            matrix[i], matrix[-i - 1] = matrix[-i - 1], matrix[i]
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.rotate(matrix))
