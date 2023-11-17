import math


class Solution:
    def mySqrt(self, x: int) -> int:
        """Квадрат(x)"""
        return int(math.sqrt(x))


x = 4
s = Solution()
print(s.mySqrt(x))