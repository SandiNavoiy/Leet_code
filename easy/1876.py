class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """"""
        new = []
        count = 0
        for i in range(len(s) - 2):
            sss = s[i : i + 3]

            if len(sss) == len(set(sss)):
                count += 1

        return count


s = "aababcabc"
sol = Solution()
print(sol.countGoodSubstrings(s))
