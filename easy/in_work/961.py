class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        """"""
        for i in nums:
            if nums.count(i) == int(len(nums) / 2):
                return i


nums = [5, 1, 5, 2, 5, 3, 5, 4]
s = Solution()
print(s.repeatedNTimes(nums))
