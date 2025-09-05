class Solution:
    def countAndSay(self, n: int) -> str:
        """"""

        def to_string(lst) -> str:
            """преобразовать вложенный список в строку"""
            s = ""
            for i in lst:
                for j in i:
                    s += str(j)
            return s

        def chastota(s: str) -> list:
            """подсчитать частоту символов"""
            lst = []
            chastota = 0
            simvol = s[0]
            for i in s:
                if i == simvol:
                    chastota += 1
                else:
                    lst.append([chastota, simvol])
                    simvol = i
                    chastota = 1
            lst.append([chastota, simvol])
            return lst

        # Базовый вариан
        s = "1"
        for i in range(n - 1):
            s = to_string(chastota(s))

        return s


s = Solution()

print(s.countAndSay(4))
