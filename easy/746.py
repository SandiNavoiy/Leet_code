class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """"""
        dp = [0] * len(cost)
        if not cost:
            return 0
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])


cost = [10, 15, 20]
s = Solution()
print(s.minCostClimbingStairs(cost))
