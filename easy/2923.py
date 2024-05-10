class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        champion = 0

        for i in range(1, len(grid)):
            if grid[i][champion] == 1:
                champion = i

        for j in range(len(grid)):
            if j != champion and grid[champion][j] == 0:
                return -1

        return champion
