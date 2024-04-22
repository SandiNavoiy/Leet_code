from itertools import combinations


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ''''''
        c = set()
        x = tuple(combinations(nums, 4))
        for i in x:
            i = list(i)
            i.sort()
            i = tuple(i)
            if sum(i) == target:
                c.add(i)
        return list(c)
nums = [-5,5,4,-3,0,0,4,-2]
target = 4
s = Solution()
print(s.fourSum(nums, target))