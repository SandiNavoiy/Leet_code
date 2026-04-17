class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        '''Подсчет двоичных подстрок'''
        ls = []
        c = 1
        #подсчет количесва последовательных символов
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                c += 1
            else:
                ls.append(c)
                c = 1
        ls.append(c)
        #счетчик двоичных подстрок
        rez = 0
        #выбираем минимальную длинну. она заведомо симметричная
        for i in range(len(ls)-1):
            rez += min(ls[i], ls[i+1])
        return rez



s = Solution()
print(s.countBinarySubstrings("00110011"))
