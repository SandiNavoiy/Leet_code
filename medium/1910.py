class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """"""
        while part in s:
            i = s.find(part)
            s = s[:i] + s[i + len(part) :]
        return s


s = "aabababa"
part = "aba"
sol = Solution()
print(sol.removeOccurrences(s, part))
