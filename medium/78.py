from itertools import combinations


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """"""
        new = []
        for i in range(len(nums) + 1):
            x = list(combinations(nums, i))
            for j in range(len(x)):
                new.append(list(x[j]))

        return new


s = Solution()
nums = [1, 2, 3]
print(s.subsets(nums))
