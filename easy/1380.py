class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        ''''''
        slov = {"a": "0", "b": "1", "c": "2", "d": "3", "e": "4", "f": "5", "g": "6", "h": "7", "i": "8", "j": "9"}
        word1, word2, word3 = "", "", ""

        for i in firstWord:
            word1 = word1 + slov[i]

        for i in secondWord:
            word2 = word2 + slov[i]

        for i in targetWord:
            word3 = word3 + slov[i]
        print(word1, word2, word3)
        return int(word1) + int(word2) == int(word3)


firstWord = "acb"
SecondWord = "cba"
targetWord = "cdb"
s = Solution()
print(s.isSumEqual(firstWord, SecondWord, targetWord))
