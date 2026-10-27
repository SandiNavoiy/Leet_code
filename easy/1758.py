class Solution:
    def minOperations(self, s: str) -> int:
        """"""
        count_0 = 0
        count_1 = 0

        for i in range(len(s)):
            t1 = "0" if i%2 == 0 else "1"
            t2 = "1" if i%2 == 0 else "0"
            if s[i] == t1:
                count_0 += 1
            elif s[i] == t2:
                count_1 += 1

        return min(count_0, count_1)



s = "0100"
sol = Solution()
print(sol.minOperations(s))
