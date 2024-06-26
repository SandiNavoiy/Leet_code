class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        """"""
        if (
            0.5
            * (
                (points[0][0] - points[2][0]) * (points[1][1] - points[2][1])
                - (points[1][0] - points[2][0]) * (points[0][1] - points[2][1])
            )
            == 0
        ):
            return False
        return True


points = [[1, 1], [2, 3], [3, 2]]
s = Solution()
print(s.isBoomerang(points))
