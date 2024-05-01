class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        ''''''
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            x = sorted(temp)

            if temp == x:
                return True
        return False

nums = [1,2, 10 ,5,7]
s = Solution()
print(s.canBeIncreasing(nums))