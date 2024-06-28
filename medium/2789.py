class Solution:
    def maxArrayValue(self, nums: list[int]) -> int:
        ''''''
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i - 1] <= nums[i]:
                nums[i - 1] = nums[i - 1] + nums[i]

        return nums[0]
nums = [2,3,7,9,3]
s = Solution()
print(s.maxArrayValue(nums))