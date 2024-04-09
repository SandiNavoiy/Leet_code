class Solution:
    def canWinNim(self, n: int) -> bool:
        """"""
        return n % 4 != 0


n = 4
s = Solution()
print(s.canWinNim(n))
