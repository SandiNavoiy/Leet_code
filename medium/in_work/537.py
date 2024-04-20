class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """"""
        num1 = complex(int(num1[0]), int(num1[2]))
        num2 = complex(int(num2[0]), int(num2[2]))
        return str(num1 + num2)


num1 = "1+1i"
num2 = "1+1i"
s = Solution()
print(s.complexNumberMultiply(num1, num2))
