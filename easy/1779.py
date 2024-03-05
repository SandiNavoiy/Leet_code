class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        """"""
        new = []
        new1 = []
        for i in points:
            if x == i[0] or y == i[1]:
                new.append(i)
        if len(new) == 0:
            return -1

        sss = abs(sum(new[0]) - (x + y))
        new1.append(new[0])
        for i in new:
            if abs(sum(i) - (x + y)) < sss:
                sss = abs(sum(i) - (x + y))
                new1.clear()
                new1.append(i)
        if len(new1) == 0:
            return -1
        return points.index(new1[0])


x = 3
y = 4
points = [[3, 4]]
s = Solution()
print(s.nearestValidPoint(x, y, points))
