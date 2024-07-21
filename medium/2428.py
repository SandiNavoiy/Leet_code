class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        ''''''
        summ = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0]) - 2):
                summ = max(summ, (grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+ 1] + grid[i+2][j+2]))

        return summ
grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
s  = Solution()
print(s.maxSum(grid))