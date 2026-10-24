class Solution:
    def isPalindromic(self, s: str) -> bool:
        """Проверка палиндрома ASCII."""

        rez = ""

        for c in s:
            rez = rez + f"{ord(c):08b}"



        return rez == rez[::-1]

#01100110

s = Solution()
print(s.isPalindromic('ff'))
