class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        """"""
        x = 0
        for i in grid:
            for j in i:
                if j > 0:
                    x += 1

        n = len(grid)
        new = [0 for a in range(n)]
        for d in grid:
            for e in range(len(d)):
                if d[e] > new[e]:
                    new[e] = d[e]

        for i in grid:
            i.sort()
            if i[-1] > 0:
                x += i[-1]

        return x + sum(new)


Grid = [[1, 0], [0, 2]]
s = Solution()
print(s.projectionArea(Grid))
