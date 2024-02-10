import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ''''''
        if n <= 0:
            return False
        return math.log2(n).is_integer()

n = 8
s = Solution()
print(s.isPowerOfTwo(n))
