class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        """"""
        banned_set = set(banned)
        l = 0
        total_sum = 0
        for i in range(1, n + 1):
            if i not in banned_set and total_sum + i <= maxSum:
                total_sum = total_sum + i
                l += 1
        return l


banned = [1, 6, 5]
n = 5
maxSum = 6
s = Solution()
print(s.maxCount(banned, n, maxSum))
