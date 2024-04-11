class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return 1 if n == 1 else 2

        shortStep, longStep = 1, 2
        minSteps = 0

        for i in range(2, n):
            minSteps = shortStep + longStep
            shortStep = longStep
            longStep = minSteps

        return minSteps


n = 3
s = Solution()
print(s.climbStairs(n))
