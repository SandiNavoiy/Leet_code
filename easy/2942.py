class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        """"""
        new = []
        for i in range(len(words)):
            if x in words[i]:
                new.append(i)
        return new
words = ["leet","code"]
x = "e"
s = Solution()
print(s.findWordsContaining(words, x))