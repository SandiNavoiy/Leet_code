import sys


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        """Returns the sum of"""

        new = []
        for i in range(n):
            ssss = 0
            for j in range(i, n):
                ssss = ssss + nums[j]
                new.append(ssss)
        new.sort()
        mod = 10**9 + 7
        return sum(new[left - 1 : right]) % mod


nums = [1, 2, 3, 4]
n = 4
left = 1
right = 5
s = Solution()
print(s.rangeSum(nums, n, left, right))
