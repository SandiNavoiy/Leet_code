class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        """"""
        col_list = 0
        col_one = 0
        for i in range(len(mat)):
            if mat[i].count(1) > col_one:
                col_one = mat[i].count(1)
                col_list = i

        return [col_list, col_one]


mat = [[0, 0, 0], [0, 1, 1]]
s = Solution()
print(s.rowAndMaximumOnes(mat))
