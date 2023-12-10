class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """"""
        if len(s) > len(t):
            x = set(s) - set(t)
        elif len(set(s)) == len(set(t)):
            return s[0]
        else:
            x = str(set(t) - set(s))
        return x[2]
s = "a"
t = "aa"
sol = Solution()
print(sol.findTheDifference(s, t))