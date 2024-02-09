class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """"""
        index = 0
        y = text.split(" ")
        for i in y:
            for j in brokenLetters:
                if j in i:
                    index += 1
                    break
        return len(y) - index


text = "hello world"
BreakedLetters = "ad"
s = Solution()
print(s.canBeTypedWords(text, BreakedLetters))
