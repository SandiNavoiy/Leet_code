class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        """"""
        rez = []
        stak = []

        for i in range(n * n):
            stak.append(i)
            if len(stak) == n:
                rez.append(stak)
                stak = []

        return rez


n = 3
s = Solution()
print(s.generateMatrix(n))
