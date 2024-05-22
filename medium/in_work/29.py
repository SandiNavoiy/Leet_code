class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """"""
        if dividend == divisor:
            return 1
        if dividend > 0 and divisor > 0:
            flag = 1
        elif dividend > 0 and divisor < 0:
            flag = 0
        elif dividend < 0 and divisor > 0:
            flag = 0
        elif dividend < 0 and divisor < 0:
            flag = 1
        elif dividend == 0:
            flag = 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        rez = 0
        while dividend > divisor:
            rez = rez + 1
            dividend = dividend - divisor
        if flag == 1:
            return rez
        else:
            return rez * -1


dividend = 1
divisor = 1
s = Solution()
print(s.divide(dividend, divisor))
