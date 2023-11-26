class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        """Максимальное произведение трех чисел"""
        nums.sort()
        print(nums)
        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[1] * nums[0])


nums = [-100, -98, -1, 2, 3, 4]
s = Solution()
print(s.maximumProduct(nums))
