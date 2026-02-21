class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]


s = Solution()
print(s.reversePrefix("abcd", 2))
