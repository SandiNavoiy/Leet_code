class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(m):
            if matrix[i][0] == 0:
                print(matrix[i])
            for j in range(n):
                pass

        return matrix
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s = Solution()
print(s.setZeroes(matrix))