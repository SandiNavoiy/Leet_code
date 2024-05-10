class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        """"""
        l = 0
        rez = []
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                x = s[i:j].swapcase()
                if set(x) == set(s[i:j]):
                    if len(s[i:j]) > l:
                        rez.clear()
                        rez.append(s[i:j])
                        l = len(s[i:j])
        if len(rez) == 0:
            return ""

        return rez[0]


s = "c"
sol = Solution()
print(sol.longestNiceSubstring(s))
