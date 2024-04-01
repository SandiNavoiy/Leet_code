class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        """"""
        ss = 0
        l = len(mat)

        if l == 1:
            return mat[0][0]
        elif l == 0:
            return 0
        elif l % 2 == 0:
            for i in range(l):
                ss = ss + mat[i][i] + mat[i][l - i - 1]
            return ss
        elif l % 2 != 0:
            for i in range(l):
                ss = ss + mat[i][i] + mat[i][l - i - 1]

            return ss - mat[int((l - 1) / 2)][int((l - 1) / 2)]


mat = [
    [7, 9, 8, 6, 3],
    [3, 9, 4, 5, 2],
    [8, 1, 10, 4, 10],
    [9, 5, 10, 9, 6],
    [7, 2, 4, 10, 8],
]
s = Solution()
print(s.diagonalSum(mat))
