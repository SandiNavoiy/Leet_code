class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        """"""

        min_x = float("inf")
        max_x = 0
        min_y = float("inf")
        max_y = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    min_x = min(min_x, i)
                    max_x = max(max_x, i)
                    min_y = min(min_y, j)
                    max_y = max(max_y, j)
        return (max_x - min_x + 1) * (max_y - min_y + 1)


grid = [[0, 1, 0], [1, 0, 1]]
s = Solution()
print(s.minimumArea(grid))
