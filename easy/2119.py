class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        """"""
        if num == 0:
            return True
        x = str(num)
        if x[-1] == "0":
            return False

        else:
            return True


num = 526
s = Solution()
print(s.isSameAfterReversals(num))
