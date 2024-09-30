class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        """"""
        rez = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j].count("0") <= k or s[i:j].count("1") <= k:
                    rez += 1

        return rez


s = "1010101"
k = 2

sol = Solution()
print(sol.countKConstraintSubstrings(s, k))
