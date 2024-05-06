class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        """"""
        grid1 = [
            [grid[0][0], grid[0][1], grid[1][0], grid[1][1]],
            [grid[0][1], grid[0][2], grid[1][1], grid[1][2]],
            [grid[1][0], grid[1][1], grid[2][0], grid[2][1]],
            [grid[1][1], grid[1][2], grid[2][1], grid[2][2]],
        ]
        for i in grid1:
            if i.count("B") != 2:
                return True
        return False


s = Solution()
grid = [["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]
print(s.canMakeSquare(grid))
