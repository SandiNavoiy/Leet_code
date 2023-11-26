class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """Умножение строк"""
        return str(int(num1) * int(num2))


num1 = "2"
num2 = "3"
s = Solution()
print(s.multiply(num1, num2))
