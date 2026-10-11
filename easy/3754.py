class Solution:
    def sumAndMultiply(self, n: int) -> int:
        '''Объединить ненулевые цифры и умножить на сумму I'''
        if n == 0:
            return 0

        ss = ""
        for i in str(n):
            if i != '0':
                ss += i

        summ = sum([int(i) for i in ss])

        return int(ss) * summ




s = Solution()
print(s.sumAndMultiply(0))
