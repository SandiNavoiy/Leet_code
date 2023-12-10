class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        """"""
        if len(nums)  < 3:
            return max(nums)
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        return nums[-3]
nums = [1,1,2]
s = Solution()
print(s.thirdMax(nums))