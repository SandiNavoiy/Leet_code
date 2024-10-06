class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        """"""
        ans = 0
        while x >= 1 and y >= 4:
            ans += 1
            x -= 1
            y -= 4
        if ans % 2 == 1:
            return "Alice"
        else:
            return "Bob"


x = 2
y = 7
s = Solution()
print(s.losingPlayer(x, y))
