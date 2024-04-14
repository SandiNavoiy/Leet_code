class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        ''''''
        ooo = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ooo = ooo + len(set(nums[i:j+1]))**2
        return ooo

nums = [1,2,1]
s = Solution()
print(s.sumCounts(nums))