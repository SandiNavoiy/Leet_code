class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """Минимальная сумма пути"""
        #решаем методами динамического програмирования
        m = len(grid)
        n = len(grid[0])


        #выбираем минимальные предудущие суумы из таблицаы посчитанных значений
        #за исключением первой строки и первого столбца. их просто суммируем. свернуть не куда
        for i in range(m):
            for j in range(n):
                if i == 0  and j  == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])



        return grid[m-1][n-1]


s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))