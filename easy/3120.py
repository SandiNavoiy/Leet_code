class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """"""

        v = set()
        for i in word:
            if ord(i) >= 97 and i.upper() in word:
                v.add(i)
        return len(v)


word = "aaAbcBC"
s = Solution()
print(s.numberOfSpecialChars(word))
