class Solution:
    def addDigits(self, num: int) -> int:
        """Добавить цифры"""
        while num > 9:
            sum = 0
            while num:
                sum += num % 10
                num = num // 10

            num = sum

        return num


num = 38
s = Solution()
print(s.addDigits(num))
