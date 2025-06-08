class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        """Уникальные пути II"""

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        rez = [[0] * (n + 1) for _ in range(m + 1)]
        rez[0][0] = 1


        for j in range(0, m):
                if obstacleGrid[0][j] == 1:
                    rez[0][j] = 0
                else:
                    rez[0][j] = 1


        for j in range(0, n):

            if obstacleGrid[j][0] == 1:
                rez[j][0] = 0
            else:
                rez[j][0] = 1

        for i in range(1, m):
                for j in range(1, n):
                    if obstacleGrid[i][j] == 0:
                        rez[i][j] = rez[i][j-1] + rez[i-1][j]
                    else:
                        rez[i][j] = 0

        print(rez)

        return rez[m - 1][n - 1]



s = Solution()

print(s.uniquePathsWithObstacles([[0,1],[0,0]]))

