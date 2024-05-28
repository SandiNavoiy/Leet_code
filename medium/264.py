class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """"""
        new = [1]
        i2 = 0
        i3 = 0
        i5 = 0

        for _ in range(1, n):
            new_i = min(new[i2] * 2, new[i3] * 3, new[i5] * 5)
            new.append(new_i)
            if new[i2] * 2 == new_i:
                i2 += 1
            if new[i3] * 3 == new_i:
                i3 += 1
            if new[i5] * 5 == new_i:
                i5 += 1
        print(new)

        return new[-1]


n = 19
s = Solution()
print(s.nthUglyNumber(n))
