class Solution:
    def countValidPrefixes(self, s: str) -> int:
        """Подсчет допустимых префиксов."""
        rez = 0

        for i in range(len(s)):
            if abs(s[:i+1].count("0") - s[:i+1].count("1")) <= 1:
                rez += 1
        return rez





s = Solution()
print(s.countValidPrefixes("00101"))
