class Solution:
    def sumBase(self, n: int, k: int) -> int:
        """"""
        summ = 0
        while n:
            summ += n % k
            n //= k
        return summ


n = 34
k = 6
s = Solution()
print(s.sumBase(n, k))
