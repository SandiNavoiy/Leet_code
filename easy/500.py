class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        new = []
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        for word in words:
            if (
                set(word.lower()) <= s1
                or set(word.lower()) <= s2
                or set(word.lower()) <= s3
            ):
                new.append(word)

        return new


words = ["Hello", "Alaska", "Dad", "Peace"]
s = Solution()
print(s.findWords(words))
