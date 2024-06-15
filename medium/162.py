class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """"""
        x = max(nums)
        return nums.index(x)


nums = [1, 2, 3, 1]
s = Solution()
print(s.findPeakElement(nums))
