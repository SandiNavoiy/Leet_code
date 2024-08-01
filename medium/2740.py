class Solution:
    def findValueOfPartition(self, nums: list[int]) -> int:
        """"""
        nums.sort()
        x = max(nums)
        for i in range(len(nums) - 1):
            x = min(nums[i + 1] - nums[i], x)

        return x


nums = [1, 3, 2, 4]
s = Solution()
print(s.findValueOfPartition(nums))
