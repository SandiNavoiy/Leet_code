class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        """"""
        new = []
        rez = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                new.append(mat[i][j])
        if len(new) != r * c:
            return mat
        else:
            for i in range(r):
                rez.append(new[c * i : c * i + c])
        return rez


mat = [[1, 2], [3, 4]]
r = 1
c = 4

s = Solution()
print(s.matrixReshape(mat, r, c))
