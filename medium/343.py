class Solution:
    def integerBreak(self, n: int) -> int:
        """"""
        if n < 4:
            return n - 1
        rez = 1
        while n > 4:
            rez = rez * 3
            n = n - 3

        return rez * n


n = 4
s = Solution()
print(s.integerBreak(n))
