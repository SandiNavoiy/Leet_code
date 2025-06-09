class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        """Уникальные пути II"""
        #расчет параметров матрицы
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        #если камень стоит сразу на первой то дальше смысла счиать нет
        if obstacleGrid[0][0] == 1:
            return 0
        #создаем мемо массив
        rez = [[0] * (n + 1) for _ in range(m + 1)]
        #делаем в первой очке 1, всегда олин путь есть
        rez[0][0] = 1
        #прогоняем первую строчку. если есть камень, но в дальнейшем везде ставим 0
        flag = 0
        for j in range(0, n):
                if obstacleGrid[0][j] == 1:
                    rez[0][j] = 0
                    flag = 1
                else:
                    if flag:
                        rez[0][j] = 0
                    else:
                        rez[0][j] = 1
        #прогоняем первый столбик. если есть камень, но в дальнейшем везде ставим 0
        flag = 0
        for j in range(0, m):


            if obstacleGrid[j][0] == 1:
                rez[j][0] = 0
                flag = 1
            else:
                if  flag:
                    rez[j][0] = 0
                else:
                    rez[j][0] = 1
        #считаем уникальные пути, если камень то обнуляем ячейку
        for i in range(1, m):
                for j in range(1, n):
                    if obstacleGrid[i][j] == 0:
                        rez[i][j] = rez[i][j-1] + rez[i-1][j]
                    else:
                        rez[i][j] = 0

        #вывод
        return rez[m - 1][n - 1]



s = Solution()

print(s.uniquePathsWithObstacles([[0,1],[0,0]]))

print(s.uniquePathsWithObstacles([[0,0]]))