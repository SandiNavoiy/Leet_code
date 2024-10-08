class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        """"""
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                t = len(s[i:j])
                if t % 2 == 0:
                    if "0" * int(t / 2) + "1" * int(t / 2) == s[i:j]:
                        ans = max(ans, j - i)

        return ans


s = "01000111"
sol = Solution()
print(sol.findTheLongestBalancedSubstring(s))
