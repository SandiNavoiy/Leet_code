from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        rez = []
        nums.sort()
        for i in range(len(nums)+1):
            x = list(combinations(nums, i))
            rez = rez + x

        return set(rez)

nums = [1,2,2]
s = Solution()
print(s.subsetsWithDup(nums))
