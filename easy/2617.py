class Solution:
    def minimizedStringLength(self, s: str) -> int:
        """Минимизировать длину строки"""
        return len(set(s))


s = "aaabc"
sol = Solution()
print(sol.minimizedStringLength(s))
