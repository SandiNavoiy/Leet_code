class Solution:
    def countElements(self, nums: list[int]) -> int:
        """"""
        x = len(nums) - nums.count(max(nums)) - nums.count(min(nums))
        if x <= 0:
            return 0

        return x


nums = [-71, -71, 93, -71, 40]
s = Solution()
print(s.countElements(nums))
