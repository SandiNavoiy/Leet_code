class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        """"""
        x = 0
        for i in words:
            if s.startswith(i):
                x += 1

        return x


words = ["a", "b", "c", "ab", "bc", "abc"]
s = "abc"
sol = Solution()
print(sol.countPrefixes(words, s))
