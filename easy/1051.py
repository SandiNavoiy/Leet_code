class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """Проверка высоты"""
        new = sorted(heights)
        col = 0
        for i in range(len(heights)):
            if heights[i] != new[i]:
                col += 1
        return col


heights = [1, 1, 4, 2, 1, 3]
s = Solution()
print(s.heightChecker(heights))
