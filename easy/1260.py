from collections import deque


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """"""
        new = []
        rez = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                new.append(grid[i][j])

        new = deque(new)
        new.rotate(k)
        new = list(new)
        for i in range(m):
            rez.append(new[i * n : i * n + n])
        return rez


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
s = Solution()
print(s.shiftGrid(grid, k))
