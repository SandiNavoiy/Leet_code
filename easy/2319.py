class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        """"""
        ss = 0
        l = len(grid)

        if l == 1:
            ss = grid[0][0]
        elif l == 0:
            ss = 0
        elif l % 2 == 0:
            for i in range(l):
                if grid[i][i] != 0 and grid[i][l - i - 1] != 0:
                    ss = ss + grid[i][i] + grid[i][l - i - 1]
                else:
                    return False

        elif l % 2 != 0:
            for i in range(l):
                if grid[i][i] != 0 and grid[i][l - i - 1] != 0:
                    ss = ss + grid[i][i] + grid[i][l - i - 1]
                else:
                    return False
            ss = ss - grid[int((l - 1) / 2)][int((l - 1) / 2)]
        ssums = 0
        for i in grid:
            ssums = ssums + sum(i)
        return ss == ssums


grid = [
    [0, 0, 0, 0, 1],
    [0, 4, 0, 1, 0],
    [0, 0, 5, 0, 0],
    [0, 5, 0, 2, 0],
    [4, 0, 0, 0, 2],
]
s = Solution()
print(s.checkXMatrix(grid))
