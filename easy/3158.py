from collections import Counter
from functools import reduce


class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        """"""
        new = [i for i in nums if nums.count(i) == 2]
        new = list(set(new))

        return reduce(lambda x, y: x ^ y, new, 0)


nums = [1, 2, 1, 3]
s = Solution()
print(s.duplicateNumbersXOR(nums))
