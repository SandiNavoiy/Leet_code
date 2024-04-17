class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        """"""
        new = str(number)
        sss = 0
        for i in range(len(new)):
            if new[i] == str(digit):
                if int(new[0:i] + new[i + 1 :]) > sss:
                    sss = int(new[0:i] + new[i + 1 :])
        return str(sss)


number = "123"
digit = "3"
s = Solution()
print(s.removeDigit(number, digit))
