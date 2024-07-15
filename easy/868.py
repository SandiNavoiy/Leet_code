class Solution:
    def binaryGap(self, n: int) -> int:
        """"""
        rez = 0
        x = bin(n)[2:]
        for i in range(len(x)):
            if x[i] == "1":
                for j in range(i + 1, len(x)):
                    if x[j] == "1":
                        rez = max(rez, j - i)
                        break

        return rez


n = 22
s = Solution()
print(s.binaryGap(n))
