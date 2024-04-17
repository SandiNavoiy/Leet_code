class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        """"""
        sss = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    if sum(mat[i]) == 1:
                        tt = 0
                        for k in range(len(mat)):
                            tt = tt + mat[k][j]
                        if tt == 1:
                            sss += 1
        return sss


mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
s = Solution()
print(s.numSpecial(mat))
