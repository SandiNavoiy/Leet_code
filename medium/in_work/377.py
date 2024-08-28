from itertools import combinations_with_replacement


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        ''''''
        new = []
        for i in range(target+1):
            x = tuple(combinations_with_replacement(nums, i))
            for j in x:

                if sum(j) == target:
                    new.append(j)

        return new
nums = [1,2,3]
target = 4
s = Solution()
print(s.combinationSum4(nums, target))