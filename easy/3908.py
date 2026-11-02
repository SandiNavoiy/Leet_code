class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        """Действительный номер цифры"""
        n = str(n)
        return n.count(str(x)) >= 1 and n[0] != str(x)


s  =Solution()
print(s.validDigit(n = 101, x = 0))
