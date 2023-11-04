class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        '''Проверьте, является ли строка аббревиатурой слов'''
        my_string = ""
        for i in words:
            my_string = my_string + i[0].lower()
        if my_string == s:
            return True
        else:
            return False





words = ["Алиса", "Боб", "Чарли"]
s = "абч"

sol = Solution()
print(sol.isAcronym(words, s))