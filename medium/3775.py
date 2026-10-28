class Solution:
    def reverseWords(self, s: str) -> str:
        '''Переверните слова с одинаковым количеством гласных.'''
        lst = s.split()
        c = sum({"a": lst[0].count("a"),
             "e": lst[0].count("e"), "i": lst[0].count("i"),"o": lst[0].count("o"),"u": lst[0].count("u")}.values())
        rez = [lst[0]]

        for i in range(1, len(lst)):
            if sum({"a": lst[i].count("a"),
             "e": lst[i].count("e"), "i": lst[i].count("i"),"o": lst[i].count("o"),"u": lst[i].count("u")}.values()) == c:
                rez.append(lst[i][::-1])
            else:
                rez.append(lst[i])



        return " ".join(rez)


s = Solution()
print(s.reverseWords("cat and mice"))
