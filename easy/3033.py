class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        ''''''
        new = [0  for i in range(max(len(matrix), len(matrix[0])))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                x = matrix[i][j]

                if x > new[j]:
                    new[j] = x
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] < 0:
                    matrix[i][j] = new[j]

        return matrix


matrix = [[3,1,1,-1,1,2],[-1,3,1,0,1,3],[-1,2,3,0,3,1],[-1,0,-1,-1,-1,1],[1,1,3,3,-1,0]]
s = Solution()
print(s.modifiedMatrix(matrix))