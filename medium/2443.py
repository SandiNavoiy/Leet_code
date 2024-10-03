class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        """"""
        sss = num
        while sss >= 0:
            if sss + int(str(sss)[::-1]) == num:
                return True
            sss = sss - 1
        return False


num = 0
s = Solution()
print(s.sumOfNumberAndReverse(num))
