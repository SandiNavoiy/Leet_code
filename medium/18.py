from itertools import combinations


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ''''''
        c = []

        x = list(combinations(nums, 4))
        for i in x:
            if sum(i) == target:
                if i not in c:
                    c.append(i)


        return c
nums = [-5,5,4,-3,0,0,4,-2]
target = 4
s = Solution()
print(s.fourSum(nums, target))