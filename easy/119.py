class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # T.C.: O(rowIndex^2) S.C.: O(rowIndex)
        ans = [1] * (rowIndex + 1)  # Filling list with 1

        # updating values with respect to pascal's triangle equation
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                ans[j] += ans[j - 1]

        return ans


rowIndex = 3
s = Solution()
print(s.getRow(rowIndex))
