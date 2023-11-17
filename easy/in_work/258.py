class Solution:
    def addDigits(self, num: int) -> int:
        """Добавить цифры"""
        while len(str(num)) > 1:
            for i in str(num):
                new = ""

                new = new + i
            print(new)

            num = new


num = 38
s = Solution()
print(s.addDigits(num))
