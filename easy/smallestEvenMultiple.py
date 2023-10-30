class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * (n % 2 + 1)


n = 5
s = Solution()
print(s.smallestEvenMultiple(n))
