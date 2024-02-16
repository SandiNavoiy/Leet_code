class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        L, ic, dc = [], 0, len(s)
        for i in s:
            if i == "I":
                L.append(ic)
                ic += 1
            else:
                L.append(dc)
                dc -= 1
        if s[-1] == "I":
            L.append(ic)
        else:
            L.append(dc)
        return L


s = "IDID"
sol = Solution()
print(sol.diStringMatch(s))
