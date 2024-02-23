class Solution:
    def averageValue(self, nums: list[int]) -> int:
        """"""
        new = [i for i in nums if i % 3 == 0 and i % 2 == 0]
        if len(new) == 0:
            return 0
        return int(sum(new) / len(new))


nums = [1, 3, 6, 10, 12, 15]
s = Solution()
print(s.averageValue(nums))
