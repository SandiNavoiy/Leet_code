import copy


class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        """"""
        primer = copy.deepcopy(mat)
        for u in range(k):
            for i in range(len(mat)):
                if i % 2 == 0:
                    temp = mat[i][0]
                    for j in range(len(mat[i]) - 1):
                        mat[i][j] = mat[i][j + 1]
                    mat[i][-1] = temp
                else:
                    temp = mat[i][-1]
                    for y in range(len(mat[i]) - 1, 0, -1):
                        mat[i][y] = mat[i][y - 1]
                    mat[i][0] = temp
        print(mat)

        return mat == primer


mat = [[1, 2]]
k = 1
s = Solution()
print(s.areSimilar(mat, k))
