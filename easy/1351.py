class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        """Подсчитайте отрицательные числа в отсортированной матрице"""
        itern = 0
        for i in grid:
            for j in i:
                if j < 0:
                    itern += 1
        return itern


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
s = Solution()
print(s.countNegatives(grid))
