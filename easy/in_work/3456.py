class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        """Найдите специальную подстроку длины K."""
        if len(s)  < 2 or k < 2:
            return True
        for i in range(len(s)-k):
            if s[i] == s[i+1] == s[i+2]:
                if i == 0 and s[i+3] !=s[i]:
                    return True
                elif i == len(s)-k and  s[i-1] !=s[i]:
                    return True
                elif s[i+3] !=s[i] and s[i-1] !=s[i]:
                    return True
        return False



## неверно. надо через сет

s = Solution()
print(s.hasSpecialSubstring(s = "aaabaaa", k = 3))
