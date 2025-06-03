class Solution:
    def canAliceWin(self, n: int) -> bool:
        """"""
        if n < 10:
            return False
        i = 10
        step = 0
        while n >= i:
            n = n - i
            i -= 1
            step += 1
        if step % 2 != 0:
            return True
        else:
            return False


n = 19
s = Solution()
print(s.canAliceWin(n))
