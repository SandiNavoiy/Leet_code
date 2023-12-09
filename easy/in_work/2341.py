class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        """"""
        new = []
        for i in nums:
            print(nums.count(i))
            if nums.count(i) == 1:
                new.append(i)
        return new
nums = [1,3,2,1,3,2,2]
s = Solution()
print(s.numberOfPairs(nums))