class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        """Returns the number of arithmetic"""
        if len(nums) < 3:
            return 0

        count = 0
        curr = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr = curr + 1
                count = count + curr

            else:
                curr = 0
        return count


nums = [1, 2, 3, 4]
s = Solution()
print(s.numberOfArithmeticSlices(nums))
