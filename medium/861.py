class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        ''''''
        rows = len(grid)
        cols = len(grid[0])
        for i in grid:
            if i[0] == 0:
                i[:] = [1 if x == 0 else 0 for x in i]

        for i in range(cols):
            temp = 0
            for j in range(rows):
                temp += grid[j][i]

            if  temp <= rows//2:

                for j in range(rows):
                    if grid[j][i] == 0:
                        grid[j][i] = 1
                    else:
                        grid[j][i] = 0

        rez = 0
        for i in grid:
            rez = rez + int("".join(map(str, i)), 2)
        return rez
grid = [[1,1,1],[0,1,0],[1,0,0],[1,0,1]]

s = Solution()
print(s.matrixScore(grid))