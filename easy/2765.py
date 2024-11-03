class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        res, c = 0, 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == (c % 2) * 2 - 1:
                c += 1
            elif nums[i] - nums[i - 1] == 1:
                c = 2
            else:
                c = 1
            res = max(res, c)
        return res if res > 1 else -1
