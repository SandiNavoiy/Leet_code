import itertools


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perm_set = itertools.permutations(nums)
        new = []
        for i in perm_set:
            new.append(list(i))
        return new


nums = [1, 2, 3]

s = Solution()
print(s.permute(nums))
