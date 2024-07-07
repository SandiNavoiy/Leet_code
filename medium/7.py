class Solution:
    def reverse(self, x: int) -> int:
        """"""
        if x < 0:
            flaf = 0
        else:
            flaf = 1
        x = str(x)[::-1]

        x = x.replace("-", "")
        x_reverse = int(x)
        if x_reverse > 2**31 - 1 or x_reverse < -(2**31):
            return 0

        if flaf == 1:
            return x_reverse
        else:
            return x_reverse * -1


x = 1534236469
s = Solution()
print(s.reverse(x))
