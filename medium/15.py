from itertools import combinations


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """"""
        seen = set()
        for i in combinations(tuple(nums), 3):

            if sum(i) == 0:
                comb_sorted = tuple(sorted(i))

                seen.add(comb_sorted)
        return list(seen)


nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
print(s.threeSum(nums))
