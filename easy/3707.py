class Solution:
    def scoreBalance(self, s: str) -> bool:
        '''Подстроки с равным баллом'''
        # алфавит
        alf = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
        new_list = []
        # список баллов
        for i in s:
            new_list.append(alf[i])

#
        S = sum(new_list)
        #НАЧАЛЬНОЕ значение суммы
        j = 0
        #сравниваем префиксную и остаток суммы
        for i in new_list:
            j += i
            if j == S-j:
                return True
        return False

s = Solution()
print(s.scoreBalance("kl"))