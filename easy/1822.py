import math


class Solution:
    def arraySign(self, nums: list[int]) -> int:
        """Знак произведения массива"""
        output1 = math.prod(nums)
        if output1 == 0:
            return 0
        elif output1 > 0:
            return 1
        else:
            return -1


nums = [-1, -2, -3, -4, 3, 2, 1]
s = Solution()
print(s.arraySign(nums))
