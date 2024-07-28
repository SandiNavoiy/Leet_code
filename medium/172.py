from math import factorial


class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''фори=мула лагранжа'''
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count


n = 1574
s = Solution()
print(s.trailingZeroes(n))
