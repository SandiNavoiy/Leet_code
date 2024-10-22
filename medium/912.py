class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """"""
        nums.sort()
        return nums


nums = [5, 2, 3, 1]
s = Solution()
print(s.sortArray(nums))
