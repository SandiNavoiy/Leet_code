class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        """Максимальная разница в продукте между двумя парами"""
        nums.sort()
        m = (nums[-1] * nums[-2]) - (nums[0] * nums[1])
        return m


nums = [5, 6, 2, 7, 4]
s = Solution()
print(s.maxProductDifference(nums))
