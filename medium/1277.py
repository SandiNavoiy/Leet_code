class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        """Подсчет квадратных подматриц со всеми единицами"""
        # выделяем длинны сторон матрицы
        n = len(matrix)
        m = len(matrix[0])
        # делаем мемо массив
        dp = [[0] * m for _ in range(n)]
        # счетчик ответа
        ans = 0
        # прогоняем первую строку
        for i in range(n):
            dp[i][0] = matrix[i][0]
        # прогоняем первый столбец
        for j in range(m):
            dp[0][j] = matrix[0][j]
        # заполняем мемо матрицу с тем условием что если в предудущих ячейках были квадраты то в эту они тоже будут учитыватся
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        #
        for i in dp:
            ans = ans + sum(i)

        return ans


matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]

s = Solution()
print(s.countSquares(matrix))
