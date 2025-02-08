class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        '''НЕОПТИМИЗИРОВАННОЕ РЕШЕНИЕ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
        rez = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)+1):
                if s[i:j].count('a')% 2 == 0 and s[i:j].count('u')% 2 == 0 and s[i:j].count('e')% 2 == 0 and s[i:j].count('i')% 2 == 0 and s[i:j].count('o')% 2 == 0:
                    rez = max(rez, len(s[i:j]))
                    print(s[i:j])


        return rez
s = "bcbcbc"

sol = Solution()
print(sol.findTheLongestSubstring(s))