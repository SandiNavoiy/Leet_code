class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        """Сумма совместимых чисел в диапазоне I"""
        ls = []
        for i in range(n - k, n + k + 1):
            if i > 0 and (n & i) == 0:
                ls.append(i)
        return sum(ls)



n = 2
k = 3
s = Solution()
print(s.sumOfGoodIntegers(n, k))

