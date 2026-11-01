class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        """Создать сетку, содержащую ровно один путь."""

        grid = [['#' for _ in range(n)] for _ in range(m)]
        i = j = 0
        for i in range (m):
            for j in range (n):
                if i == 0 or j == n-1:
                    grid[i][j] = "."

        return [''.join(row) for row in grid]


s = Solution()
print(s.createGrid(m = 3, n = 3))
