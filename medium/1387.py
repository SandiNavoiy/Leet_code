class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """"""
        new = {}
        for i in range(lo, hi + 1):
            step = 0
            ccc = i
            while i > 1:
                if i % 2 == 0:
                    i = i // 2
                else:
                    i = 3 * i + 1
                step = step + 1
            new[ccc] = step
        new = sorted(new.items(), key=lambda item: item[1])
        return new[k - 1][0]


lo = 12
hi = 15
k = 2
s = Solution()
print(s.getKth(lo, hi, k))
