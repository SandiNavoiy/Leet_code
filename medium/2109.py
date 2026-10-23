class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        '''Добавление пробелов в строку'''
        rez = []
        i = 0
        for idx in range(len(s)):
            if idx != spaces[i]:
                rez.append(s[idx])
            else:
                rez.append(" ")
                rez.append(s[idx])
                if i < len(spaces) - 1:
                    i = i +1


        return "".join(rez)


s = Solution()
print(s.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
