from statistics import median


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """"""
        med = median(nums)
        low = [i for i in nums if i < med]
        high = [i for i in nums if i >= med]

        return high


nums = [1, 2, 3, 4, 5]
s = Solution()
print(s.rearrangeArray(nums))
