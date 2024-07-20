class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        """"""
        new = []
        for word in words:
            if len(set(word)) == len(set(pattern)) == len(set(zip(word, pattern))):
                new.append(word)


        return new
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
s = Solution()
print(s.findAndReplacePattern(words, pattern))