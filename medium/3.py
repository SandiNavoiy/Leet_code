class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """"""
        rez = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(s[i:j]) == len(set(s[i:j])):
                    rez = max(rez, len(s[i:j]))
                else:
                    break
        return rez
s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
