class Solution:
    def concatHex36(self, n: int) -> str:
        """ """
        hex16 = "0123456789ABCDEF"
        hex36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        def toBase(x, b, hex):
            """перевод числа в другую систему счисления"""
            s= []
            while x > 0:
                s.append(hex[x % b])
                x //= b
            return "".join(s[::-1])
        n2 = n**2
        n3 = n**3
        return (toBase(n2, 16, hex16) + toBase(n3, 36, hex36))



s = Solution()
print(s.concatHex36(13))
