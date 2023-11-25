class Solution:
    def thousandSeparator(self, n: int) -> str:
        """Разделитель тысяч"""
        str_n = str(n)
        if len(str_n) <= 3:
            return str_n
        else:
            y = str_n[::-1]

            new = ""
            for i in range(len(y)):

                if  i % 3 == 0 and i != 0:
                    new = new + "." + y[i]
                else:
                    new = new + y[i]

        return new[::-1]
n = 1234
s = Solution()
print(s.thousandSeparator(n))
