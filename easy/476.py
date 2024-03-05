class Solution:
    def findComplement(self, num: int) -> int:
        """"""
        x = bin(num)[2:]
        y = ""
        for i in x:
            if i == "1":
                y = y + "0"
            else:
                y = y + "1"

        return int(y, 2)


num = 5

s = Solution()
print(s.findComplement(num))
