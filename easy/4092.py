class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        """Двоичный цифровой балл"""
        print(bin(a))
        print(bin(b))
        a = bin(a).count('1')
        b = bin(b).count('1')

        print(a,b)
        if a >= b:
            return a * b
        else:
            return b // a





s = Solution()
print(s.calculateScore(5, 15))
