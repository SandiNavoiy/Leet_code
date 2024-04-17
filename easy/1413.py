class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        temp = min(nums)
        if temp > 0:
            return 1
        else:
            return -temp + 1


nums = [-3, 2, -3, 4, 2]
s = Solution()
print(s.minStartValue(nums))
