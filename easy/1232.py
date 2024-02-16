class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        """"""
        coordinates.sort()
        x = abs(coordinates[1][0] - coordinates[0][0])
        y = abs(coordinates[1][1] - coordinates[0][1])

        if len(coordinates) == 1:
            return True
        for i in range(len(coordinates) - 1):
            if (
                coordinates[i][0] + x != coordinates[i + 1][0]
                or coordinates[i][1] + y != coordinates[i + 1][1]
            ):
                return False
        return True


coordinates = [[2, 4], [2, 5], [2, 8]]
s = Solution()
print(s.checkStraightLine(coordinates))
