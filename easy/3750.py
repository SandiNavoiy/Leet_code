class Solution:
    def minimumFlips(self, n: int) -> int:
        '''Минимальное количество переворотов для инвертирования двоичной строки.'''

        s = bin(n)[2:]
        s1 = s[::-1]
        rez = 0
        for i in range(len(s)):
            if s[i] != s1[i]:
                rez += 1
        return rez
s = Solution()
print(s.minimumFlips(7))