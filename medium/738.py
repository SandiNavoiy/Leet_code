class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = str(n)
        N = len(n)

        for i in range(N - 1):
            if n[i] > n[i + 1]:
                break
        else:
            return int(n)

        while i > 0 and n[i] == n[i - 1]:
            i -= 1

        return int(str(int(n[: i + 1]) - 1) + "9" * (N - i - 1))


n = 332
s = Solution()
print(s.monotoneIncreasingDigits(n))
