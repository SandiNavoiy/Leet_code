from functools import reduce
from operator import xor


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        ''''''

        return (reduce(xor, nums)^k).bit_count()
nums = [2, 1, 3, 4]
k = 1
s = Solution()
print(s.minOperations(nums, k))