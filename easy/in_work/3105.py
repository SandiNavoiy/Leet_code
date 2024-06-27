class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        ''''''
        ybuv = 0
        vozrast = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i]:
                vozrast = vozrast + 1
        for i in range(len(nums)-1):
            pass
nums = [1,4,3,3,2]
s = Solution()
print(s.longestMonotonicSubarray(nums))