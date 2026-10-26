from typing import List

class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:

        top = x
        bottom = x + k - 1

        while top < bottom:
            for j in range(y, y + k):
                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]

            top += 1
            bottom -= 1

        return grid




s = Solution()
print(s.reverseSubmatrix(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] , x = 1, y = 0, k = 3))
