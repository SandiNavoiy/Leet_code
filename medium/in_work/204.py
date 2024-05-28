class Solution:
    def countPrimes(self, n: int) -> int:
        """"""
        new = []
        if n <= 10:
            for i in range(2, n):
                if i == 2 or i == 3 or i == 5 or i == 7:
                    new.append(i)
        else:
            new = [2, 3, 5, 7]
            for i in range(11, n, 2):
                if all(i % p != 0 for p in new):
                    new.append(i)

        return len(new)


n = 499979
s = Solution()
print(s.countPrimes(n))
