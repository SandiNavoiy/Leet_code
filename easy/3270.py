class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        """"""

        def pp(x):
            if len(str(x)) == 4:
                return str(x)
            elif len(str(x)) == 3:
                return "0" + str(x)
            elif len(str(x)) == 2:
                return "00" + str(x)
            elif len(str(x)) == 1:
                return "000" + str(x)

        num1 = pp(num1)
        num2 = pp(num2)
        num3 = pp(num3)
        rez = ""

        for i in range(4):
            rez = rez + str(min(int(num1[i]), int(num2[i]), int(num3[i])))

        return int(rez)


num1 = 1
num2 = 10
num3 = 1000
s = Solution()
print(s.generateKey(num1, num2, num3))
