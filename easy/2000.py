class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """Reverse Prefix of Word"""
        o = word.find(ch)
        if o > 0:
            str_new = word[o::-1] + word[o + 1 : :]
            return str_new
        else:
            return word


word = "abcdefd"
# "dcbaefd"
ch = "d"

s = Solution()
print(s.reversePrefix(word, ch))
