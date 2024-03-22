class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        for l in range(int(area**0.5), 0, -1):
            if area % l == 0:
                return [area // l, l]



area = 122122
s = Solution()
print(s.constructRectangle(area))