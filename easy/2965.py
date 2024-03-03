class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        """"""
        zero = 0
        two = 0
        n = len(grid) * len(grid)
        new = []
        for i in grid:
            for j in i:
                new.append(j)

        for i in range(0, n + 1):
            if new.count(i) == 0:
                zero = i
            if new.count(i) == 2:
                two = i
        rez = []
        rez.append(two)
        rez.append(zero)
        return rez


grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
s = Solution()
print(s.findMissingAndRepeatedValues(grid))
