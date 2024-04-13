class Solution:
    def arrangeCoins(self, n: int) -> int:
        ''''''
        i = 1
        rez = 0
        while i < n:
            rez = rez +i
            v = n - rez
            i += 1
            print(v)
            if v < i:
                break
        if n== 1:
            return 0
        return i-1
n = 5
s = Solution()
print(s.arrangeCoins(n))
