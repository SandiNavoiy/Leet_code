class Solution:
    def countAsterisks(self, s: str) -> int:
        """Подсчитайте звездочки"""
        v = 0
        sum = 0
        for i in range(len(s)):
            if s[i] == "|":
                v = v + 1
            if v % 2 == 0:
                if s[i] == "*":
                    sum = sum + 1
        return sum


s = "l|*e*et|c**o|*de|"

sol = Solution()
print(sol.countAsterisks(s))
