class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Первый уникальный символ в строке"""
        nn = 0
        for i in range(len(s)):

            if s.count(s[i]) == 1:
                nn = i
                return nn

        return -1

s = "leetcode"
sol = Solution()
print(sol.firstUniqChar(s))