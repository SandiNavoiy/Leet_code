class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        """Процент букв в строке"""
        sun = 0
        for i in s:
            if i == letter:
                sun += 1
        return 100 * sun // len(s)


s = "foobar"
letter = "o"
sol = Solution()
print(sol.percentageLetter(s, letter))
