class Solution:
    def convertDateToBinary(self, date: str) -> str:
        """"""
        god = bin(int(date[0:4]))[2:]
        mes = bin(int(date[5:7]))[2:]
        den = bin(int(date[8:10]))[2:]

        return str(god) + "-" + str(mes) + "-" + str(den)


date = "2100-12-31"
s = Solution()
print(s.convertDateToBinary(date))
