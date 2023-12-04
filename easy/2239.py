class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        """"""
        new = []
        for i in nums:
            new.append(abs(i))
        x = new.index(min(new))


        return nums[x]

nums = [2,-1,1]
s = Solution()
print(s.findClosestNumber(nums))
