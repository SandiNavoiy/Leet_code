from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """"""
        new = []
        c = dict(Counter(nums))
        for i, j in c.items():
            if j == 1:
                new.append(i)
        return new


nums = [1, 2, 1, 3, 2, 5]
s = Solution()
print(s.singleNumber(nums))
