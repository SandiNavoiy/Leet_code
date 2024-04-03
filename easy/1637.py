class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        """"""
        points.sort(key=lambda x: x[0])
        rez = 0
        for i in range(1, len(points)):
            if points[i][0] - points[i - 1][0] > rez:
                rez = points[i][0] - points[i - 1][0]

        return rez


points = [[1, 5], [1, 70], [3, 1000], [55, 700], [999876789, 53], [987853567, 12]]
s = Solution()
print(s.maxWidthOfVerticalArea(points))
