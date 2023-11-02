class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        """Перестановка строки"""
        outcome = ""
        for i in range(len(s)):
            outcome = outcome + s[indices.index(i)]
        return outcome


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
sol = Solution()
print(sol.restoreString(s, indices))

print(s[0])
