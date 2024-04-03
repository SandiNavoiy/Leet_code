class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """"""
        new = sentence.split()
        for i in range(len(new)):
            if searchWord in new[i][: len(searchWord)]:
                return i + 1

        return -1


sentence = "hellohello hellohellohello"
searchWord = "ell"
s = Solution()
print(s.isPrefixOfWord(sentence, searchWord))
