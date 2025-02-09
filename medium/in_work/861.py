class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        ''''''
        rows = len(grid)
        cols = len(grid[0])
        for i in grid:
            if i[0] == 0:
                i[:] = [1 if x == 0 else 0 for x in i]



        return grid
grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]

s = Solution()
print(s.matrixScore(grid))