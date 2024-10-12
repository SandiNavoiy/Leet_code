from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        ''''''

        ans  = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[i-j].append(mat[i][j])



        for i in ans.keys():
            ans[i].sort()



        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = ans[i - j].pop(0)

        return mat
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
s = Solution()
print(s.diagonalSort(mat))