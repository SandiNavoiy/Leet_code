class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """"""
        per = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    per = per + 4
                    if i > 0 and grid[i - 1][j] == 1:
                        per -= 2

                    if j > 0 and grid[i][j - 1] == 1:
                        per -= 2
        return per


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
s = Solution()
print(s.islandPerimeter(grid))
