class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        """монотонный массив"""

        if all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)):
            return True

        elif all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)):
            return True
        else:
            return False


nums = [6, 5, 4, 4]
s = Solution()
print(s.isMonotonic(nums))
