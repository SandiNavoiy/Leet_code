class Solution:
    def countPrimes(self, n: int) -> int:
        """"""
        new = [x for x in range(0, n)]
        NN = len(new)
        if len(new) > 1:
            new[1] = 0
        i = 1
        while i < NN:
            if new[i] != 0:
                j = i + i
                while j < NN:
                    new[j] = 0
                    j = j + i
            i = i + 1
        rez = [x for x in new if x != 0]
        return len(rez)



n = 499979
s = Solution()
print(s.countPrimes(n))
