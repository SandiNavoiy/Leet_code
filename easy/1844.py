class Solution:
    def replaceDigits(self, s: str) -> str:
        """Замените все цифры символами"""
        new_s = ""
        for i in range(len(s)):
            if i % 2 == 0:
                new_s = new_s + s[i]
            else:
                new_s = new_s + chr(ord(s[i - 1]) + int(s[i]))

        return new_s


s = "a1b2c3d4e"
sol = Solution()
print(sol.replaceDigits(s))
