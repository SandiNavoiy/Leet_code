class Solution:
    def scoreOfString(self, s: str) -> int:
        """"""
        eee = 0
        for i in range(len(s) - 1):
            eee += abs(ord(s[i + 1]) - ord(s[i]))
        return eee


s = "hello"
sol = Solution()
print(sol.scoreOfString(s))
