class Solution:
    def numberOfSteps(self, num: int) -> int:
        """"""
        x = 0
        while num > 0:
            x += 1
            if num % 2 == 0:
                num = num / 2

            else:
                num -= 1

        return x


num = 14
s = Solution()
print(s.numberOfSteps(num))
