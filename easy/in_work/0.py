from itertools import combinations


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """"""
        inn = []
        seen = set()
        for i in combinations(nums, 3):
            comb_sorted = tuple(sorted(i))
            if sum(comb_sorted) == 0 and comb_sorted not in seen:
                inn.append(comb_sorted)
                seen.add(comb_sorted)

        return inn


nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
print(s.threeSum(nums))
