class Solution:
    def findValidPair(self, s: str) -> str:
        """"""
        rez = ""
        for i in range(len(s) - 1):
            if s[i] != s[i + 1] and (
                s.count(s[i]) == int(s[i]) and s.count(s[i + 1]) == int(s[i + 1])
            ):
                rez = s[i] + s[i + 1]
                break

        return rez


s = "2523533"

sol = Solution()
print(sol.findValidPair(s))
