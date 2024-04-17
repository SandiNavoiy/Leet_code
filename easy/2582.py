class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """"""
        if time < n:
            return time + 1
        elif (time // (n - 1)) % 2 == 0:
            print(1)

            return time % (n - 1) + 1
        else:
            print(2)
            return n - time % (n - 1)


n = 18
time = 38


s = Solution()
print(s.passThePillow(n, time))
