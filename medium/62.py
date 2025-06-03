class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Уникальные пути"""
        # решаем методами динамического програмирования
        rez = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                rez[i][j] = rez[i][j - 1] + rez[i - 1][j]

        print(rez)
        return rez[m - 1][n - 1]


s = Solution()
print(s.uniquePaths(1, 1))
