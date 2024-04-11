class Solution:
    def numberOfCuts(self, n: int) -> int:
        """"""
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n % 2 == 0:
            return int(n / 2)
        else:
            return n


n = 4
s = Solution()
print(s.numberOfCuts(n))
