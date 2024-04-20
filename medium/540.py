class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        n= nums[0]
        for i in nums[1:]:
            n^= i
            print(n)
        return n
nums = [1,1,2,3,3,4,4,8,8]
s = Solution()
print(s.singleNonDuplicate(nums))