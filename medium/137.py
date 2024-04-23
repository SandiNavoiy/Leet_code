from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """"""
        c = dict(Counter(nums))
        for i, j in c.items():
            if j == 1:
                return i


nums = [2, 2, 3, 2]
s = Solution()
print(s.singleNumber(nums))
