class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if i >= x:
                    dp[i] += dp[i - x]
        return dp[-1]


nums = [1, 2, 3]
target = 4
s = Solution()
print(s.combinationSum4(nums, target))
