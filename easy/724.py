class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """"""
        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[i + 1 :]):
                return i
        return -1


nums = [1, 7, 3, 6, 5, 6]
s = Solution()
print(s.pivotIndex(nums))
