import math


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        n = n * 2


        chet= sum([n for n in range(1, n+1) if n % 2 == 0])
        nechet = sum([n for n in range(1, n+1) if n % 2 != 0])



        return math.gcd(chet, nechet)




s = Solution()
print(s.gcdOfOddEvenSums(4))