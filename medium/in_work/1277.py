class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        ''''''
        N = min(len(matrix), len(matrix[0]))
        def proverka(mat):
            """проверка матрицы на единица"""
            razmer = len(mat)
            temp = 0
            for i in mat:
                temp = temp + sum(i)
            if temp == razmer*2:
                return True
            else:
                return False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):




matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

s = Solution()
print(s.countSquares(matrix))