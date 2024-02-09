class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        """"""
        new = []
        for i in nums:
            new.append(nums.count(i))
        new.sort()
        index = max(new)
        return new.count(index)


nums = [1, 2, 2, 3, 1, 4]
s = Solution()
print(s.maxFrequencyElements(nums))
