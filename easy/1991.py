
class Solution:
        def findMiddleIndex(self, nums: list[int]) -> int:

            if len(nums) == 1:
                return 0
            if 0 == sum(nums) - nums[0] :
                return 0
            for i in range(1, (len(nums))):
                if sum(nums[0:i]) == sum(nums[i + 1:]):

                    return i


            return -1
nums = [1,1]
s = Solution()
print(s.findMiddleIndex(nums))