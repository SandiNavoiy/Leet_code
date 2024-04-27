class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        ''''''
        tt = 0
        for i in range(1, len(nums)-1):

            if max(nums[0:i]) <nums[i] > max(nums[i+1:]) :
                tt = tt + 1
            elif max(nums[0:i]) == nums[i] == max(nums[i+1:]) and max(nums[i+1:]) > min(nums[i+1:]) and max(nums[0:i]) > min(nums[0:i]):
                tt = tt + 1
            print(tt)
            if max(nums[0:i]) > nums[i] < max(nums[i+1:]):
                tt = tt + 1
        return tt

nums = [8,2,5,7,7,2,10,3,6,2]
s = Solution()
print(s.countHillValley(nums))