class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        ''''''
        pov  = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                box = grid[i][j]
                if box!= 0:
                    pov  = pov + box * 4 + 2
                    if i > 0:


                        pov = pov - min(box, grid[i-1][j])*2
                    if j > 0:

                        pov = pov - min(box, grid[i][j-1])*2

        return pov
grid = [[2,2,2],[2,1,2],[2,2,2]]
s = Solution()
print(s.surfaceArea(grid))