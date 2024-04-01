class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        """"""
        ss = str(x)
        sums = 0
        for i in ss:
            sums = sums + int(i)

        if x % sums == 0:
            return sums
        else:
            return -1


x = 18
s = Solution()
print(s.sumOfTheDigitsOfHarshadNumber(x))
