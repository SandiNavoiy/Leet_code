class Solution:
    def minCost(self, n: int) -> int:
        ''''''

        if n == 1:
            return 0
        else:

            return (n-1) + self.minCost(n-1)
s = Solution()
print(s.minCost(3))