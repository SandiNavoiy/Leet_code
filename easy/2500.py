class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        """"""
        sss = 0
        y = 0

        while len(grid[0]) > 0:
            new = []
            for i in grid:
                i.sort()
                x = i.pop(-1)
                new.append(x)

            y = y + max(new)

        return y


grid = [[1, 2, 4], [3, 3, 1]]

s = Solution()
print(s.deleteGreatestValue(grid))
