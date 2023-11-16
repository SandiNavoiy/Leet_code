class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Длина последнего слова"""
        words = s.split()
        if words:
            return len(words[-1])
        else:
            return 0

s = "   fly me   to   the moon  "

sol = Solution()
print(sol.lengthOfLastWord(s))
