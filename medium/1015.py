class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """"""
        if not k % 2 or not k % 5:
            return -1
        prev = 0
        for i in range(1, k + 1):
            prev = (prev * 10 + 1) % k
            if prev == 0:
                return i
        return -1


k = 3
s = Solution()
print(s.smallestRepunitDivByK(k))
