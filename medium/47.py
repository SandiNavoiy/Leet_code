import itertools


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        perm_set = itertools.permutations(nums)
        new = []
        for i in perm_set:
            if list(i) not in new:
                new.append(list(i))
        return new


nums = [1, 1, 2]

s = Solution()
print(s.permuteUnique(nums))
