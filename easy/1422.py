class Solution:
    def maxScore(self, s: str) -> int:
        """"""
        summ = 0

        for i in range(1, len(s)):
            if (s[0:i].count("0") + s[i:].count("1")) > summ:
                summ = s[0:i].count("0") + s[i:].count("1")

        return summ


s = "011101"
sol = Solution()
print(sol.maxScore(s))
