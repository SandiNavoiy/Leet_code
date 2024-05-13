class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """"""

        temp = nums[0]
        rez = nums[0]
        for i in range(1, len(nums)):
            temp = max(temp + nums[i], nums[i])

            rez = max(rez, temp)
        return rez


nums = [1]
s = Solution()
print(s.maxSubArray(nums))
