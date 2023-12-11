class Solution:
    def minimizedStringLength(self, s: str) -> int:

        return len(set(s))

s = "aaabc"
sol = Solution()
print(sol.minimizedStringLength(s))