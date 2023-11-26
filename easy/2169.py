class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        """"""
        it = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 = num1 - num2
                it = it + 1
            else:
                num2 = num2 - num1
                it = it + 1
        return it


num1 = 2
num2 = 3

s = Solution()
print(s.countOperations(num1, num2))
