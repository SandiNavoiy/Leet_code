class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        ''''''
        for i in range(len(grid)):
           for j in range(len(grid[0])):

               if i+1 < len(grid) and grid[i][j] != grid[i + 1][j]:
                   return False
               if j+1 < len(grid[0]) and grid[i][j] == grid[i][j + 1]:
                   return False

        return True
grid = [[1,0,2],[1,0,2]]
s = Solution()
print(s.satisfiesConditions(grid))