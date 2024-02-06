class Solution:
    def sumZero(self, n: int) -> list[int]:
        ''''''
        new = []
        if n % 2 == 0:
          new = [x for x in range(1, int(1+n/2))] + [-x for x in range(1, int(1+n/2))]
        else:
            new = [x for x in range(1, int(1+ n/2))] + [-x for x in range(1, int(1 + n/2))] + [0]
        return new
n = 10
s = Solution()
print(s.sumZero(n))