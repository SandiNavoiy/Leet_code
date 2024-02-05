class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        """"""
        x = 0
        for i in patterns:
            if i in word:
                x += 1
        return x


patterns = ["a", "abc", "bc", "d"]
word = "abc"
s = Solution()
print(s.numOfStrings(patterns, word))
