class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        ''''''
        if n <= 9:
            return n
        while n > 9:
            flag = 0
            x = str(n)
            for i in range(len(x)-1):
                if x[i] > x[i+1]:
                    n = n - 1
                    flag = 1
                    break

            if flag == 0:
                return n

        return 9
n = 332
s = Solution()
print(s.monotoneIncreasingDigits(n))