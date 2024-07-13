class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        """Returns the maximum"""
        rez = 0

        new = list(zip(*grid))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rez = rez + min(max(grid[i]), max(new[j])) - grid[i][j]

        return rez


grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
s = Solution()
print(s.maxIncreaseKeepingSkyline(grid))
