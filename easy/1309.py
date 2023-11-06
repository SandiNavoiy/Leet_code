class Solution:
    def freqAlphabets(self, s: str) -> str:
        """разшифровка"""
        for i in range(26, 0, -1):
            s = s.replace(str(i) + '#' * (i > 9), chr(96 + i))
        return s
s = "1326#"

sol = Solution()
print(sol.freqAlphabets(s))
