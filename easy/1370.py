class Solution:
    def sortString(self, s: str) -> str:
        """"""
        new = ""
        www = set(s)
        www = list(www)
        www = sorted(www)
        rrr = sorted(www, reverse=True)
        www = "".join(www)
        rrr = "".join(rrr)
        while len(s) > len(new):
            new = new + www
            new = new + rrr

        return new[: len(s)]


s = "leetcode"
sol = Solution()
print(sol.sortString(s))
