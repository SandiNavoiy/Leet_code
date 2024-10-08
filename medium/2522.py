class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        """"""
        ans = 1
        temp = 0
        for i in s:
            if int(i) > k:
                return -1
            temp = 10 * temp + int(i)
            if temp > k:
                ans += 1
                temp = int(i)
        return ans


s = "165462"
k = 60
sol = Solution()
print(sol.minimumPartition(s, k))
