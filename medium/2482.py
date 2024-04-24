class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        ''''''
        srtoki = []
        stolb = [0 for i in range(len(grid[0]))]

        for i in range(len(grid)):
            srtoki.append(grid[i].count(1))
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    stolb[j] = stolb[j] +1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = srtoki[i] + stolb[j] - (len(srtoki) - srtoki[i]) - (len(stolb) - stolb[j])
        return grid
grid = [[1,1,1],[1,1,1]]
s = Solution()
print(s.onesMinusZeros(grid))