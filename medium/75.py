from collections import Counter


class Solution:
    def sortColors(self, nums):
        nums[:] = [0] * nums.count(0) + [1] * nums.count(1) + [2] * nums.count(2)


nums = [2, 0, 2, 1, 1, 0]
s = Solution()
print(s.sortColors(nums))
