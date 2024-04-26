class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        ''''''
        new = [[0]*len(colSum) for x in range(len(rowSum)) ]


        for i in range(0,len(rowSum)):
            for j in range(0,len(colSum)):
                new[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] = rowSum[i] - new[i][j]
                colSum[j] = colSum[j] - new[i][j]

        return new
rowSum = [3,8]
colSum = [4,7]
s = Solution()
print(s.restoreMatrix(rowSum, colSum))