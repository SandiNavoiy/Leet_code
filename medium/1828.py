class Solution:
    def countPoints(
        self, points: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        """"""
        rez = []
        for i in queries:
            n = 0
            for j in points:
                if (j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2 <= i[2] ** 2:
                    n = n + 1

            rez.append(n)

        return rez


points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
s = Solution()
print(s.countPoints(points, queries))
# [2,3,2,4]
