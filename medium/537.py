class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """"""
        a1, b1 = num1.split('+')
        a2, b2 = num2.split('+')
        if "+-" in num1 or "+-" in num2:
            flaf = 1
        else:
            flaf = 0

        num1 = complex(int(a1), int(b1[:-1]))
        num2 = complex(int(a2), int(b2[:-1]))
        rez = num1 * num2

        if rez.real == 0:
            rez = str(rez)
            rez = rez.replace("j", "i")
            return "0+" + rez
        else:
            if rez.imag <0:

                return str(int(rez.real)) + "+" + str(int(rez.imag)) + "i"


            else:
                rez = str(rez)
                rez = rez.replace("j", "i")
                return rez[1:-1]





num1 = "20+22i"
num2 = "-18+-10i"
s = Solution()
print(s.complexNumberMultiply(num1, num2))
