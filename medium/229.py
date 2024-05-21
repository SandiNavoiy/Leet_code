from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        """"""
        n = int(len(nums) / 3)
        new = set()
        for i in nums:
            if nums.count(i) > n:
                new.add(i)
            if len(new) > 2:
                break

        return list(new)


nums = [3, 2, 3]
s = Solution()
print(s.majorityElement(nums))
