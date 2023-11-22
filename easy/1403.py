class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        """"""
        nums.sort(reverse=True)

        new = []
        for i in range(len(nums)):
            if sum(new) <= sum(nums[i::]):
                new.append(nums[i])
        return new
nums = [4,3,10,9,8]
s = Solution()
print(s.minSubsequence(nums))