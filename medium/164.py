class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        """"""
        max_razn = 0
        nums.sort()
        n = len(nums)
        if n <= 2:
            return 0
        for i in range(n - 1):
            max_razn = max(max_razn, nums[i + 1] - nums[i])

        return max_razn


nums = [3, 6, 9, 1]
s = Solution()
print(s.maximumGap(nums))
