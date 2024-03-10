class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        """"""
        new = []
        for i in rectangles:
            new.append(min(i))
        x = max(new)

        return new.count(x)


rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
s = Solution()
print(s.countGoodRectangles(rectangles))
