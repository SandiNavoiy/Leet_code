class Solution:
    def checkRecord(self, s: str) -> bool:
        """"""
        n = 0
        if s.count("A") < 2 and "LLL" not in s:
            return True
        return False


s = "PPALLP"
sol = Solution()
print(sol.checkRecord(s))
