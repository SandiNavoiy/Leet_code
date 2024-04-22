class Solution:
    def minOperations(self, n: int) -> int:
        """"""
        tt = 0
        arr = []
        for i in range(0, n):
            arr.append((2 * i) + 1)
        target = int(sum(arr) / n)
        for i in arr:
            tt = tt + abs(target - i)

        return int(tt / 2)


n = 3

s = Solution()
print(s.minOperations(n))
