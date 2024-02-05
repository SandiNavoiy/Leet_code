from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """Сила четырех"""
        if n <= 0:
            return False
        return n > 0 and log(n, 4).is_integer()


n = 4
s = Solution()
print(s.isPowerOfFour(n))
