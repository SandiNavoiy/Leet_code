class Solution:
    def reformatNumber(self, number: str) -> str:
        """"""
        new = []
        number = number.replace(" ", "")
        number = number.replace("-", "")
        while len(number) > 0:
            if len(number) == 4:
                new.append(number[0:2])
                new.append(number[2:4])
                number = ""
            elif len(number) == 2:
                new.append(number[0:2])
                number = ""
            else:
                new.append(number[0:3])
                number = number[3:]

        return "-".join(new)


number = "123 4-567"
s = Solution()
print(s.reformatNumber(number))
