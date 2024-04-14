class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        res =0
        for x in nums:
            res |= x
        return res*(2**(len(nums)-1))


        return
nums = [5,1,6]
s = Solution()
print(s.subsetXORSum(nums))