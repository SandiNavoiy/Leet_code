class Solution:
    def isValid(self, word: str) -> bool:
        """"""
        glass = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        gl = 0
        l = 0
        sogl = 0

        for i in word:
            if not i.isalpha() and not i.isdigit():
                return False
            if i.isalpha() or i.isdigit():
                l = l + 1
            if i in glass:
                gl = gl + 1
            if i.isalpha() and i not in glass:
                sogl = sogl + 1

        if l >= 3 and sogl >= 1 and gl >= 1:
            return True
        return False


word = "234Adas"
s = Solution()
print(s.isValid(word))
