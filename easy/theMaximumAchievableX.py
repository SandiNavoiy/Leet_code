class Solution:
    """Найдите максимально достижимое число
"""
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return  num + 2 * t
num = 3
t = 2
s = Solution()
print(s.theMaximumAchievableX(num, t))