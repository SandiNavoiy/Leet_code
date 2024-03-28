class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        """"""
        rez = 0
        for i in range(1, len(points)):
            rez = rez + max(
                abs(points[i][0] - points[i - 1][0]),
                abs(points[i][1] - points[i - 1][1]),
            )

        return rez


points = [[1, 1], [3, 4], [-1, 0]]
s = Solution()
print(s.minTimeToVisitAllPoints(points))
