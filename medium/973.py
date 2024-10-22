import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """"""
        points.sort(key=lambda x: math.dist(x, [0, 0]))
        return points[0:k]


points = [[1, 3], [-2, 2]]
k = 1
s = Solution()
print(s.kClosest(points, k))
