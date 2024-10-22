class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        ret = []
        while n != 0:
            if n % 2 == 0:
                ret.append("0")
                n //= -2
            else:
                ret.append("1")
                n = (n - 1) // -2

        return "".join(ret[::-1])


n = 2
s = Solution()
print(s.baseNeg2(n))
