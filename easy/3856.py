class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        ''''''
        glass = ["a", "e", "i", "o", "u"]
        new = list(s)
        while new and new[-1] in glass:
            new.pop()
        return "".join(new)
s = Solution()
print(s.trimTrailingVowels("idea"))